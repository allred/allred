select customername, count(*) from customers c, orders o
where o.customerid = c.customerid
group by c.customername
