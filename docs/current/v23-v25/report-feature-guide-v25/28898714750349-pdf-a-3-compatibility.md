---
title: "PDF/A-3 Compatibility"
id: 28898714750349
section: "Report Feature Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898714750349-PDF-A-3-Compatibility
updated_at: 2026-02-26T02:14:11Z
source_host: docs-report.zendesk.com
---
# 
PDF/A-3 Compatibility

PDF/A-3 represents a restricted variant of Adobe PDF version 1.7 (as defined in ISO 32000-1). It is specifically designed for the archival of page-oriented documents, a purpose for which PDF is already widely employed. In comparison to its predecessor, PDF/A-2 (ISO 19005-2), PDF/A-3 introduces a singular and highly significant feature: the ability to embed files, regardless of their format, within a PDF/A file. This innovation surpasses the limitations of PDF/A-2, which only permitted the inclusion of other PDF/A files.

The following features are indispensable for regions and regulatory requirements:

- PDF/A Standard Compliance: As illustrated in the screenshot below, when a PDF file adheres to the PDF/A standard, you will observe a compliance message at the top of the PDF report.
			

- Support for PDF Attachments: As shown in the screenshot above, you can view attachments in the sidebar and easily access them.
            

- Formula support on above properties.
            

To attain the above functionality, you can configure your reports using Designer, Web Report Studio, or Page Report Studio. Please note that these properties are applicable to all fields except chart or map fields.

In Designer, configure properties as below steps:

- Incorporate attachments into a report and link them to a specific field, and configure the properties of Ignore When No Attachment, PDF Attachment, PDF Attachment Name.
            

- Export the report to PDF, and select/clear PDF/A compliant.
            

In Web Report Studio, go to Edit Mode and open Inspector.

- Incorporate attachments into a report and link them to a specific field, and configure the properties of Ignore When No Attachment, PDF Attachment, and PDF Attachment Name.
            

- Select/clear PDF/A Compliant when exporting to PDF.

In Page Studio, go to Interactive Mode, select a field, and view its properties.

- Incorporate attachments into a report and link them to a specific field, and configure the properties of Ignore When No Attachment, PDF Attachment, and PDF Attachment Name.
            

- Select/clear PDF/A Compliant when exporting to PDF.

For running or scheduling existing reports on Server, select/clear PDF/A Compliant as the same.

- In section 6.1.3 of ISO 19005-1:2005 specifications, one of the PDF/A standards, it explicitly states that encryption is not allowed for PDF/A documents. Consequently, the Encrypt option and the PDF/A compliant option cannot be selected simultaneously. To clarify, if the Encrypt option is chosen initially, the PDF/A compliant option will become disabled; conversely, if the PDF/A compliant option is selected first, the Encrypt option will be disabled. If both encryption and PDF/A compliance are specified through the API, an exception will be triggered.
            

- When both the Split and PDF/A options are designated, the Split option will take precedence, and PDF/A compliance will be disregarded. This behavior arises because PDF/A relies on Accessible PDF, which can conflict with the Split option.
