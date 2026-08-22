---
title: "Inserting a Formula, Summary, Parameter, or a WHERE Portion"
id: 1500009562222
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562222-Inserting-a-Formula-Summary-Parameter-or-a-WHERE-Portion
updated_at: 2021-07-24T05:56:22Z
---

# Inserting a Formula, Summary, Parameter, or a WHERE Portion

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582601-Inserting-a-Business-View)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582641-Creating-and-Modifying-a-Query)

# Inserting a Formula, Summary, Parameter, or a WHERE Portion

The following methods are used to insert a formula, summary, parameter or a WHERE portion into a catalog and to return the handle of the newly inserted object:

* insert(String formulaName, String desc, String expression)
* insert(String summaryName, String desc, int functionType, String fieldName, String groupByFld)
* insert(String parameterName, String desc, String prompt, String type, String default Value)
* insert(String wherePortionName, String desc, WherePortionInfo whereportionInfo)

**Parameters**

* formulaName - The name of the formula.
* desc - The description of the object.
* expression - The expression.
* summaryName - The name of the summary.
* functionType - The type of the function.
* fieldName - The field name calculated on.
* groupByFld - The field name grouped by.
* parameterName - The parameter Name.
* prompt - The input text prompt.
* type - The parameter data type.
* defaultValue - The defaultValue of the parameter.
* wherePortionName - The WHERE portion name.
* whereportionInfo - The WHERE portion information.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582601-Inserting-a-Business-View)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582641-Creating-and-Modifying-a-Query)
