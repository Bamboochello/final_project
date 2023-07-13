SELECT co.login,
               COUNT(ord."inDelivery")
FROM "Couriers" AS co
INNER JOIN "Orders" AS ord ON co.id=ord."courierId"
WHERE ord."inDelivery" = true
GROUP BY co.login;

SELECT track,
              CASE
                         WHEN "Orders".finished = true THEN 2
                         WHEN "Orders".cancelled = true THEN -1
                         WHEN "Orders"."inDelivery" = true THEN 1
                     ELSE 0
                 END AS status
FROM "Orders";
