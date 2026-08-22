---
title: "Inheriting Styles"
id: 1500009593241
section: "Applying National Language Support - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009593241-Inheriting-Styles
updated_at: 2021-07-24T05:53:41Z
---

# Inheriting Styles

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571262-Applying-Styles)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593101-Defining-Report-Security)

# Inheriting Styles

The four types of data components - table, crosstab, chart, and banded object in a page report - can remember the style applied to them and therefore their style can be inherited by another component or a new segment inserted into them.

When inserting a component or a new segment into a table, crosstab, chart, or banded object, by default the former will inherit the style from the latter. However, when inserting a table, crosstab, chart, or banded object via the component creation dialog into a table or banded object, Logi JReport provides you with the opportunity to cancel the way of inheriting style and instead specify a new style to the component. In this case, the inserted component reserves its own style independent from the style of the parent data component.

An option Inherit Style is provided for enabling a table, crosstab, chart, or banded object to inherit the style from a parent table or banded object. It is available:

* In the component creation wizard when inserting a table, crosstab, chart, or banded object into a table or banded object.
* In the Style screen of the wizard of a table, crosstab, chart, or banded object which is in a table or banded object.
* In the style drop-down list on the Home menu tab. The Inherit Style here only works on the objects which are in a table, crosstab, chart, or banded object.

When modifying the style of one of the four types of data components, if the child component's style type is Inherit Style, it will change to apply the new style accordingly. However if the child component has a style, it will reserve its own style.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571262-Applying-Styles)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593101-Defining-Report-Security)
