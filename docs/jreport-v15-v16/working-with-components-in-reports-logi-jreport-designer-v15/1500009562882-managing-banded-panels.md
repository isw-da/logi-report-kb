---
title: "Managing Banded Panels"
id: 1500009562882
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562882-Managing-Banded-Panels
updated_at: 2021-07-24T05:56:10Z
---

# Managing Banded Panels

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562862-Managing-Data-of-a-Banded-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583261-Embedding-Data-Components-in-a-Banded-Object)

# Managing Banded Panels

By default, a banded object consists of these panels: a Banded Header (BH) panel, a Banded Page Header (BPH) panel, a Detail (DT) panel, a Parallel Detail (PDT, this is only for the banded objects which are created on HDS) panel, a Banded Page Footer (BPF) panel, a Banded Footer (BF) panel, and several Group Header (GH) and Group Footer (GF) panels if the data in the banded object is grouped.

Logi JReport Designer allows you to perform the following tasks related to the banded panels.

* **Adding a banded panel**  
   Select a panel of the same type, right-click it and select **Insert Panel After**. A blank panel of the same type will be inserted into the banded object. This can be useful for making sure that formulas in a panel are executed in the correct order.
* **Deleting a banded panel**  
   To delete a banded panel from a banned object, right-click the panel and select **Delete**. Note that you cannot delete a panel of a certain type if it is the only one of that type.
* **Hiding a banded panel**  
   To hide a banded panel from view, right-click the panel, and then select **Hide**.
* **Showing a hidden banded panel**
  1. Check the item **Hidden Objects** on the View tab, and the hidden panel will then be displayed and marked with two triangles.
  2. Right-click the banded panel, and select **Show** on the shortcut menu to release its hidden state.
  3. Turn off **Hidden Objects** on the View menu as it will not show you a true view of your report.
* **Resizing a banded panel**
  + For a vertical or cross banded object, drag the boundary below the banded panel until the panel is at the required height.
  + For a horizontal banded object, drag the boundary on the right side of the banded panel until the panel is at the required width.

You can also make use of the properties Invisible and Width/Height of a banded panel in the Report Inspector to show/hide, and resize the panel.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562862-Managing-Data-of-a-Banded-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583261-Embedding-Data-Components-in-a-Banded-Object)
