---
title: "Information Bus Dialog"
id: 1500009632041
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009632041-Information-Bus-Dialog
updated_at: 2021-07-24T16:04:27Z
---

# Information Bus Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608802-Incremental-Condition-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632081-Insert-Aggregation-Dialog)

# Information Bus Dialog

The Information Bus dialog helps you to edit the Information Bus content saved with user information in the current catalog. It appears when you select File > Information Bus.

![Information Bus dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916786071/infmtnbus.gif)

Information Bus is a built-in object in Logi Report containing information from information containers of three levels: global level, organization level and user level. System admin can get or put information in all information containers. Organization admin can get or put information in the global level information container, its own organization level information container and the user level information containers that belong to its organization. Organization user can get or put information in the global level information container, the organization level information container it belongs and its own user level information container.

**Information container list**

Shows a tree structure according to the user definition in the information containers in the current catalog. The users here are the same as those created for [business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500009605382-Business-View-Security).

**Information box**

Displays information created for the selected information container, which are key-value pairs of information that can be put or got by authorized users when calling APIs and writing formulas with the following functions:

* [GetInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#GetInfo)
* [GetOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#GetOrgInfo)
* [GetUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#GetUserInfo)
* [PutInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#PutInfo)
* [PutOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#PutOrgInfo)
* [PutUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#PutUserInfo)
* [RemoveInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#RemoveInfo)
* [RemoveOrgInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#RemoveOrgInfo)
* [RemoveUserInfo()](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#RemoveUserInfo)

To edit information for a container, select it from the container list, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the information box. In the Key and Value cells, double-click to specify the key and value respectively. To remove an information line, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif).

**OK**

Applies the changes and closes this dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608802-Incremental-Condition-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632081-Insert-Aggregation-Dialog)
