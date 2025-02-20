SELECT 
    c.customerName, 
    c.phone, 
    c.city, 
    c.state, 
    c.country, 
    o.orderDate, 
    o.status, 
    p.productName, 
    od.quantityOrdered
FROM FIL_DB.FIL_SCHEMA.customers c
JOIN FIL_DB.FIL_SCHEMA.orders o ON c.customerNumber = o.customerNumber
JOIN FIL_DB.FIL_SCHEMA.orderdetails od ON o.orderNumber = od.orderNumber
JOIN FIL_DB.FIL_SCHEMA.products p ON od.productCode = p.productCode
WHERE o.status = 'Pending'
ORDER BY o.orderDate DESC