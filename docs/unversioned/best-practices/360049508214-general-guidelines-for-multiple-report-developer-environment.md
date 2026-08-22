---
title: "General Guidelines for Multiple Report Developer Environment"
id: 360049508214
section: "Best Practices"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049508214-General-Guidelines-for-Multiple-Report-Developer-Environment
updated_at: 2020-07-27T22:39:55Z
---

# General Guidelines for Multiple Report Developer Environment

### Problem

It's common for more than one report developer to work on report development, and each developer is typically assigned to create a certain number of reports and work individually.  After initial development work is completed, you may also want to merge the reports each of them created into a central catalog so you do not have to maintain multiple catalogs.

### Solution

Here are two best practice scenarios for merging catalogs:

Scenario 1:  
  
To merge different catalogs together, you will use the "Save To" function inside of Logi Report Designer. For more detailed information of how to use the "Save To" feature, please refer to Report documentation: <https://documentation.logianalytics.com/logireportdesignerguidev17/content/html/catalog/ctlg_merge.htm>  
  
To effectively use "Save To" feature, make sure the original catalog and the target catalog file have the exact same name. If the catalogs are named differently by each individual report developer, you can rename them before you proceed to the catalog merge, and it won't break any reports which may have already been created, as the name of the catalog is not maintained in the report.

Scenario 2:

Create a naming convention document to give to each report developer before they even start their work. The naming convention document should tell them how should they name the resources used in the report, including query, formula, summary and parameters.  The uniqueness of the mapping name rules applies within the same data source.  For example, during the catalog merge, if it detects there are multiple formulas with the same name in the original catalog as well the target catalog, it will ask you to rename one of them, which adds more difficulties during the merge.
