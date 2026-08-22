---
title: "How to set a Page Header only for the first page of the Page Report?"
id: 360049996494
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049996494-How-to-set-a-Page-Header-only-for-the-first-page-of-the-Page-Report
updated_at: 2020-07-27T23:01:51Z
---

# How to set a Page Header only for the first page of the Page Report?

**Question:**

What property do I set to make the Page Header appear only once on the first page of a Page Report?

**Answer:**

You can use a formula applied to the **Invisible** property on Page Header to achieve the goal. Here are the steps:  
  
Step 1: Open the specific report and highlight the Page Header of the report. Then go to **Inspector** and locate the property called **Invisible**. See the screenshot below:  
  
![](/attachments/token/GNgO2c9omCS0KI0Xo9UFiKsjp/?name=inline1029947260.png)​  
Step 2:  Click the **FX** button of the **Invisible** property and create a new formula. The formula can be written as:  
  
pagenumber;  
pagenumber  !=  1  
  
![](/attachments/token/MhcsNzi05UL4OcqNtrA17Pfbe/?name=inline-274644057.png)​  
Step 3:  Save the formula and close the Formula Editor. The formula should be applied to the Page Header.  
  
![](/attachments/token/iZJuVCbnZBGoq7xDqoIMZXuhp/?name=inline1686549287.png)​  
Step 4: Run the report. The page header only shows on the first page of your report.
