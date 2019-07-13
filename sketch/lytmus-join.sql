-- find 5 recommendations (of different cateogory) from similar orders
-- which are in stock, order by frequency ordered descending
use shopping_db;
select * from product, 
  (
  select product_id, count(product_id) as freq from order_product
    where order_id in ( 
      select order_id from order_product
        where product_id = 91
      )
    and product_id != 91
    group by product_id
  ) as product_freq
  where
  product.id = product_freq.product_id
  and product.stock > 0
  and product.category != (select category from product where id = 91)
  order by product_freq.freq desc, product.id
  limit 5
