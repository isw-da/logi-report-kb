---
title: "Edit View Element Dialog"
id: 1500010065781
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065781-Edit-View-Element-Dialog
updated_at: 2021-07-24T10:38:56Z
---

# Edit View Element Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030642-Edit-Values-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030662-Elasticsearch-Connection-Wizard-Dialog)

# Edit View Element Dialog

The Edit View Element dialog helps you to [edit the specified view element](https://devnet.logianalytics.com/hc/en-us/articles/1500010034562-Creating-Business-Views-in-a-Catalog#Element). It appears when you right-click any view element of a business view and select Edit from the shortcut menu in the Catalog Manager.

The dialog contains two tabs: [General](#General) and [Security](#Security).

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain changes and closes the dialog.

**Help**

Displays the help document about this feature.

## General

Sets properties for the view element.

![Edit View Element dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404901264791/edtvwelmnt_gen.gif)

**Display Name**

Specifies the display name of the view element. An intuitive display name can help end users easily understand the element.

**Mapping Name**

Specifies the mapping name of the field to which the view element is mapped. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) to select the field.

**Type**

Specifies the [type](https://devnet.logianalytics.com/hc/en-us/articles/1500010034582-Business-View-Elements) of the view element: Group, Aggregation or Detail.

**By Expression**

Available only when the type of the view element is defined as Group. It specifies whether to use an expression to retrieve values for the group element. When the option is checked, Mapping Name is disabled.

* **Settings**  
   Opens the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010066181-Formula-Editor-Dialog) to compose the expression.

**Aggregate Function**

Available only when the view element is an aggregation. It specifies the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function) for the aggregation object. When DistinctSum is selected, the following option is available and should be set:

* **Distinct On**  
   Specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010032562-Select-Fields-Dialog) dialog.

**Customized**

Available only when the type of the view element is defined as Aggregation. If checked, you can create a [custom aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500010034582-Business-View-Elements#CA) by writing a formula.

* **Settings**  
   Opens the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010066181-Formula-Editor-Dialog) to compose a formula using resources in the current business view, which can return an aggregation.

**Tip**

Specifies the tooltip of the view element, which will be shown when end users hover the mouse pointer over it in the business view resource tree at server runtime.

**Description**

Specifies the description of the view element.

## Security

Specifies user accessibility to elements of the business views in the current catalog data source.
For details about options in the tab, refer to the [Edit Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010065501-Edit-Business-View-Security-Dialog) dialog.

![Edit View Element dialog - Security tab](https://devnet.logianalytics.com/hc/article_attachments/4404909222039/edtvwelmnt_scrty.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030642-Edit-Values-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030662-Elasticsearch-Connection-Wizard-Dialog)
