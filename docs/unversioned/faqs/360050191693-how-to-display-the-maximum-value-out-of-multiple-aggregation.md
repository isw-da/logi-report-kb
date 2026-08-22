---
title: "How to display the Maximum value out of multiple aggregation fields?"
id: 360050191693
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050191693-How-to-display-the-Maximum-value-out-of-multiple-aggregation-fields
updated_at: 2020-07-27T22:29:22Z
---

# How to display the Maximum value out of multiple aggregation fields?

**Question:**

How do I display the maximum value out of multiple aggregation fields?

**Answer:**

To achieve the goal, users can write a custom aggregation and use it in a crosstab report.  Follow these steps:

1. Create a new **Crosstab** style report. In the screenshot below, the "@Customer\_Country" field is specified in the **Columns** section.  The "Sum of @Cost" and "Sum of @Unit Price" fields are specified in the **Summaries** section.
2. In the **Resources** box of the wizard, click "New Crosstab Formula", create a formula ("Formula1" in below example). The formula is defined as:

   ```
   number summaries[]  = [@(@Customers_Country:current, sum(@Cost)), @(@Customers_Country:current, sum(@"Unit Price"))];  
     
   return maximum(summaries);
   ```

     
   ![](/attachments/token/0ovVd1Xt4WHOUWJcYBbxvz8Ts/?name=inline-792733114.png)
3. Insert the formula into the **Summaries** box, as shown in the screenshot below.  Exit the wizard.![](/attachments/token/1WtZz0ZFUQsGv9b87Z8NZsKmE/?name=inline1040147114.png)
4. Run the report.  The screenshot below displays the intended visual result; i.e. the red section contains the maximum values from the aggregate values in the previous rows.![](/attachments/token/7lmwGp8XQte9QXfKIUKhSXAQS/?name=inline1742871665.png)

**Further Reading**

<https://documentation.logianalytics.com/logireportdesignerguidev17/content/customagg/cstmagg.htm?Highlight=custom%20aggregation>
