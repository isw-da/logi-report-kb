---
title: "Enter Parameter Values Dialog"
id: 1500009586681
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586681-Enter-Parameter-Values-Dialog
updated_at: 2021-07-24T05:55:22Z
---

# Enter Parameter Values Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586661-Encrypt-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565442-Enter-Values-Dialog)

# Enter Parameter Values Dialog

The Enter Parameter Values dialog appears when you preview, print or export a report with parameters, or preview a query that contains parameters. In this dialog, all the parameter names used in the report or query and the prompting information are listed. [See the dialog](javascript:%20void(null)).

![Enter Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889365527/enterprmvlu.gif)

The way to specify a parameter value varies with the type and properties of the parameter. Here are several ways you can use to specify parameter values:

* In the parameter value combo box, select the required one from the drop-down list or input the value manually.
* Select or unselect the checkbox to specify a Yes/No value.
* Select the button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to specify multiple values in the [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009565442-Enter-Values-Dialog) dialog.
* Select the calendar button ![](https://devnet.logianalytics.com/hc/article_attachments/4404889299735/btn_clndr.gif) to specify a date and time value using either calendar or expression in the [Calendar](https://devnet.logianalytics.com/hc/en-us/articles/1500009564742-Calendar-Dialog) dialog. If you [use an expression to specify the value](https://devnet.logianalytics.com/hc/en-us/articles/1500009590141-Using-Built-in-Functions-to-Set-Date-and-Time-Parameter-Values), when you hover the mouse pointer over this value, a tip will appear showing its expression. Select on the value, the expression will be displayed in the value text box and you can edit the expression in the text box directly if you want. After editing, when you select elsewhere outside of the value text box:
  + If the edited expression is correct, a new value calculated by the expression will be displayed in the parameter value text box.
  + If the edited expression is wrong, no value will be created and the expression itself will be displayed and highlighted in red in the value text box. Correct the expression, or select the calendar button to specify a value.

**OK**

Applies your input and runs the report/previews the query.

**Default**

Accepts the default value and runs the report/previews the query.

**Cancel**

Cancels your operation and exits running the report/previewing the query.

**Help**

Displays the help document about this feature.

**Note:** You are recommended not to use blank as the thousands separator in Number-typed parameter values under French locale, otherwise your input will not be correctly recognized because of a JVM bug. For details, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586661-Encrypt-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565442-Enter-Values-Dialog)
