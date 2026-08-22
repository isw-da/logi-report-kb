---
title: "Page Report Properties"
id: 12480364969869
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480364969869-Page-Report-Properties
updated_at: 2026-03-03T14:27:50Z
source_host: docs-report.zendesk.com
---
# 
Page Report Properties

This topic describes the properties of a Page Report object.

 A page report may contain one or more report tabs. By default, the root node in the report structure tree  represents the current report tab. You can select Forward on the Report Inspector toolbar to show the page report as the root node (if the current root node represents the report body of the current report tab, you need to select the button twice). After showing the page report node in the Report Inspector, you can select the node to set its properties.

| Property Name | Description |
| --- | --- |
| General (available for query-based page report) |  |
| Class Type | Shows the class type of the object. Read only. |
| Instance Name | Shows the instance name of the object. Read only. |
| Others |  |
| Constrained Data | Specifies whether to constrain users to use the business views the page report applies only, if they need to add more data components into the report at runtime. Data type: Boolean |
| Import Parameter Values | Specifies the name of a class name with the full package name, from which to import default values for the parameters the page report applies, when you set Parameter List Auto to "false". See Importing Parameter Values. Data type: String |
| Parameter List Auto | Specifies whether to get the default values for the parameters the page report applies from the values you have defined in the catalog. When you set this property to "false", Report Engine gets the default parameter values from the class file you specify via the Import Parameter Values property. Data type: Boolean |
| Cache Image | Specifies whether to cache images at runtime. Image cache is enabled only when this property is true and the system system property -DimageCacheEnable is true (default true when not set). Data type: Boolean |
| Push Down Group Query | Specifies whether to push down group level summary computations in the page report to the database at runtime. Choose an option from the drop-down list. default Select to apply the setting for the Push Down Group Query property of the query each data component in the report uses correspondingly. true Select to push down group level summary computations to the database if it can do the computations; otherwise, Report Engine performs the computations itself. false Select to let Report Engine perform group level summary computations itself. Data type: Enumeration |
