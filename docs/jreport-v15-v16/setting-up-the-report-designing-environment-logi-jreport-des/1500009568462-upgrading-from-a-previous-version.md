---
title: "Upgrading from a Previous Version"
id: 1500009568462
section: "Setting Up the Report Designing Environment - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568462-Upgrading-from-a-Previous-Version
updated_at: 2021-07-24T05:54:33Z
---

# Upgrading from a Previous Version

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589841-Solving-Installation-Problems) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589801-Logi-JReport-Designer-Launch-Files)

# Upgrading from a Previous Version

Reports created in Logi JReport Designer 7 or prior must be converted to Version 15 before they can be modified with Logi JReport Designer 15. The conversion procedure is described below. However, Logi JReport Version 7 or prior reports can continue to be published to, and run by Logi JReport Server 15 without any modifications.

**To upgrade Version 7.1 or prior reports to Version 15:**

1. Be sure that Logi JReport Designer 15 has been installed in a folder that does not contain any previous versions of Logi JReport Designer. If it does, uninstall and reinstall to a new directory.
2. Convert a set of reports by either of following methods:
   * Run the conversion tool [rptconv.bat/rptconv.sh](https://devnet.logianalytics.com/hc/en-us/articles/1500009589801-Logi-JReport-Designer-Launch-Files#rptconv.bat) which is located in `<install_root>\bin`.
   * Convert a report by opening it directly and then saving it with Logi JReport Designer 15.

A Version 7 or prior report is converted to a flow layout report with a [banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009562842-Banded-Objects). A banded object has the same report sections that a Version 7 or prior report template has, however in Version 15 the sections are called panels. Any other data objects in the Version 7 or prior report are converted to the corresponding data components within the banded object.

All converted reports can be used in the same way as a new Version 15 report that contains a banded object. You can insert other components into the banded panels as described in [Component placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports). In addition, the features of Version 15, such as page mode, display types, CSS styles and so on can be applied to the converted reports. However, in the converted reports, the layout cannot extend beyond the banded object as it can for a new report created in Version 15. That is, while you can insert components into the banded object created as a result of the migration, you cannot insert components after the banded object. If your reports require this functionality, you will need to re-create the report as a new report in Version 15.

**Note:** Migrated reports need to be analyzed to determine how Version 15 functionality can best be applied. For example, converted reports that share a dataset should be combined into page reports to take full advantage of Version 15 performance improvements. Contact Jinfonet Professional Services for assistance if desired.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589841-Solving-Installation-Problems)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589801-Logi-JReport-Designer-Launch-Files)
