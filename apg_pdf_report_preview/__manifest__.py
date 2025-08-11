{
    "name": "Open PDF Reports and PDF Attachments in Browser",
    "version": "18.0.0.0",
    "summary": """
   Enables users to preview PDF reports directly in the browser instead of downloading them immediately, enhancing user experience and saving time when reviewing documents.
""",
    'description' : """The PDF Report Preview module provides an intuitive and user-friendly feature that allows users to view reports in-browser without the need to download them each time. This improves workflow efficiency, especially when dealing with large volumes of report generation or frequent validations.""",
    "author": "Apagen Solutions Pvt Ltd",
    'Company': 'Apagen Solutions Pvt Ltd',
    'Maintainer' : 'Apagen Solutions Pvt Ltd',
    "category": "Productivity",
    "license": "LGPL-3",
    "website": "https://www.apagen.com",
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
            "apg_pdf_report_preview/static/src/js/tools.esm.js",
            "apg_pdf_report_preview/static/src/js/report.esm.js",
        ],
    },
    'images': ['static/description/banner.jpg'],
    "installable": True,
    "application": False,
    "auto_install": False,
}
