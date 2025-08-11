import json
import re
from email.utils import encode_rfc2231
from typing import Any

from werkzeug import urls
from werkzeug.wrappers import Response

from odoo import http
from odoo.http import request, route
from odoo.tools.safe_eval import safe_eval
from odoo.tools.safe_eval import time as safe_time

from odoo.addons.web.controllers.report import ReportController


class CxReportController(ReportController):
    def _get_extra_context_for_single_record(self, report_name, ignore_expr=None):
        ignore_expr = ignore_expr or []
        extra_ctx = {}
        for expr in re.findall(r"%.?\(.*?\)", report_name):
            expr = expr.replace("%", "").strip()[1:-1].strip()
            if "." in expr:
                expr = expr.split(".")[0]
            if expr in ignore_expr:
                continue
            extra_ctx[expr] = "report"
        return extra_ctx

    def _compose_report_file_name(self, docids, report):
        report_name = "report"
        if docids:
            records = request.env[report.model].browse(docids)
            record_count = len(docids)
            if record_count == 1 and report.sudo().print_report_name:
                # Single record
                print_report_name = report.sudo().print_report_name
                extra_ctx = self._get_extra_context_for_single_record(
                    print_report_name,
                    ignore_expr=["object", "time"],
                )
                report_name = safe_eval(
                    print_report_name,
                    {
                        "object": records,
                        "time": safe_time,
                        **extra_ctx,
                    },
                )
            else:
                # Multiple records
                report_name = f"{report.name} x{record_count}"
        else:
            report_name = report.name
        return report_name

    # ------------------------------------------------------
    # Report controllers
    # ------------------------------------------------------
    @route(
        [
            "/report/<converter>/<reportname>",
            "/report/<converter>/<reportname>/<docids>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def report_routes(
        self,
        reportname: str,
        docids: str | None = None,
        converter: str | None = None,
        **data: dict[str, Any],
    ) -> Response:
        """Handle report routes with browser preview for PDFs."""
        if converter != "pdf":
            return super().report_routes(
                reportname, docids=docids, converter=converter, **data
            )

        report = request.env["ir.actions.report"]._get_report_from_name(reportname)
        if not report:
            return request.not_found()

        context = dict(request.env.context)

        # Handle options and context
        if data.get("options"):
            options_str = data.pop("options")
            if isinstance(options_str, str):
                data.update(json.loads(urls.url_unquote_plus(options_str)))

        if data.get("context"):
            context_str = data.get("context")
            if isinstance(context_str, str):
                context.update(json.loads(urls.url_unquote_plus(context_str)))

        # Handle company context
        cid = data.get("cid")
        if cid:
            try:
                allowed_company_ids = [int(cid) for cid in cid.split(",")]
                context["allowed_company_ids"] = allowed_company_ids
            except (ValueError, AttributeError):
                return request.not_found()

        request.env.context = context

        # Handle document IDs
        doc_ids: list[int] = []
        if docids:
            try:
                doc_ids = [int(i) for i in docids.split(",")]
                records = request.env[report.model].browse(doc_ids)
                records.check_access_rule("read")
            except (ValueError, AttributeError):
                return request.not_found()

        report_name = self._compose_report_file_name(doc_ids, report)
        pdf = report.with_context(**context)._render_qweb_pdf(
            reportname, doc_ids, data=data
        )[0]

        return request.make_response(
            pdf,
            headers=[
                ("Content-Type", "application/pdf"),
                ("Content-Length", len(pdf)),
                (
                    "Content-Disposition",
                    f"inline; filename*={encode_rfc2231(report_name, 'utf-8')}.pdf",
                ),
            ],
        )

    @http.route("/report/check_wkhtmltopdf", type="json", auth="user")
    def check_wkhtmltopdf(self):
        return request.env["ir.actions.report"].get_wkhtmltopdf_state()
