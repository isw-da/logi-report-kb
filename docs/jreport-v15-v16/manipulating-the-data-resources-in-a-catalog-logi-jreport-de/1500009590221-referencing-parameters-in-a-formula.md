---
title: "Referencing Parameters in a Formula"
id: 1500009590221
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590221-Referencing-Parameters-in-a-Formula
updated_at: 2021-07-24T05:54:29Z
---

# Referencing Parameters in a Formula

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568602-Parameter-Application-Cases)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590161-Dynamically-Filtering-Queries)

# Referencing Parameters in a Formula

A formula which references parameters will return values according to the parameter values. To reference a parameter in a formula, follow the syntax: *@ParameterName*.

In the following example, a formula will be used to display the URL for a company, which is based on the value of the parameter p\_Company.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the desired data source and create a type-in parameter named p\_Company of String type (leave the other settings to their default).
3. In the same data source, [create a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula) named CompanyURL in the Formula Editor as follows:

   `"http://www." + @p_Company + ".com"`

   Here, you can either manually type @p\_Company, or you can select it from the Parameters node in the Fields panel (if you choose this option, the @ sign will be automatically inserted).
4. Insert the formula into a report.
5. View the report result, and type the string **Jinfonet** when prompted to enter the parameter value for p\_Company. You will then find that the value of the formula becomes http://www.jinfonet.com.

There may be times you need to display the value of a multi-valued parameter. The built-in function [join](https://devnet.logianalytics.com/hc/en-us/articles/1500009568262-String-Functions#join) assists with that. For example, the following expression will show a list of selected states separated by commas:

`"Selected States : " +  trim(join (@pStates,",")) + "\r\n"`

These are simple examples of referencing parameters in formulas, in which the formulas are placed directly into a report. You would better understand the benefits of referencing parameters in formulas which are used to [control object properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568602-Parameter-Application-Cases)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590161-Dynamically-Filtering-Queries)
