---
title: "Cached Report Bursting"
id: 1500011463701
section: "Logi JReport Feature Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463701-Cached-Report-Bursting
updated_at: 2021-07-24T10:39:44Z
---

# Cached Report Bursting

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431682-Business-View-Security) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431662-Record-Level-and-Column-Level-Security)

# Cached Report Bursting

Cached report bursting is a group level security that controls group data availability to users. Report designer writes formulas to control user access to specific values of a group and set the formulas to the security properties of the group in a table or banded object: Grant (also taken as users), Groups, and Roles. It also applies to nested groups.

Cached report bursting is a group level security that controls group data availability to users. A report designer can write formulas to control user access to specific values of a group and set the formulas to the security properties of the group in a table or banded object: Grant (also taken as users), Groups, and Roles. It also applies to nested groups.

The following is a formula example which states that the returned user1 is able to access Canada of the Country group and user2 Mexico.

`if (@Country == "Canada")
  
return "user1";
  
if (@Country == "Mexico")
  
return "user2";`

The formula name can be set as the Grant property value of the Country group in a table or banded object:

![Cached Report Bursting](https://devnet.logianalytics.com/hc/article_attachments/4404901356055/rptscrty_burst.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431682-Business-View-Security) [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431662-Record-Level-and-Column-Level-Security)
