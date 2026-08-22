---
title: "Upgrading Reports from v7 or Prior to v17"
id: 1500009611302
section: "Setting Up the Report Designing Environment - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009611302-Upgrading-Reports-from-v7-or-Prior-to-v17
updated_at: 2021-07-24T16:03:54Z
---

# Upgrading Reports from v7 or Prior to v17

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634321-Solving-Installation-Problems) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634281-Using-the-Designer-Launch-Files)

# Upgrading Reports from v7 or Prior to v17

After you upgrade your Logi Report Designer from v7 or prior to v17, you must convert the reports created in the old Designer to v17 before you can modify them with Logi Report Designer v17. However you can continue to publish v7 or prior reports to Logi Report Server v17 and run the reports on the server without any modifications. This topic describes how you can upgrade v7 or prior reports to v17.

1. Be sure that you have installed Designer v17 in a folder that does not contain any previous versions of Logi Report Designer. If it does, uninstall and reinstall to a new directory.
2. Convert a set of reports by either of following methods:
   * Run the conversion tool [rptconv.bat/rptconv.sh](https://devnet.logianalytics.com/hc/en-us/articles/1500009634281-Using-the-Designer-Launch-Files#rptconv.bat) which is located in `<install_root>\bin`.
   * Convert a report by opening it directly and then saving it with Designer v17.

Logi Report Designer converts a v7 or prior report to a flow layout report with a [banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009628361-Banded-Objects). A banded object has the same report sections that a v7 or prior report template has, however in v17 the sections are called panels. Any other data objects in the v7 or prior report are converted to the corresponding data components within the banded object.

You can use the converted reports in the same way as with a new v17 report that contains a banded object. You can insert other components into the banded panels as described in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports). In addition, you can apply the new features of v17, such as Page Mode, Display Type, CSS Style, and so on to the converted reports. However, in the converted reports, the layout cannot extend beyond the banded object as it can for a new report created in v17. That is, while you can insert components into the banded object created as a result of the migration, you cannot insert components after the banded object. If your reports require this functionality, you will need to re-create the report as a new report in v17.

**Note:** Migrated reports need to be analyzed to determine how v17 functionality can best be applied. For example, converted reports that share a dataset should be combined into page reports to take full advantage of v17 performance improvements. Contact Logi Analytics Support at [support@logianalytics.com](mailto:support@logianalytics.com) for assistance if desired.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634321-Solving-Installation-Problems) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634281-Using-the-Designer-Launch-Files)
