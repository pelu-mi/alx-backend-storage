-- Task 4 for MySQL Advanced
-- SQL script: Trigger that decreases the quantity of an item
-- after adding an order
DROP TRIGGER IF EXISTS item_count;
DELIMITER $$
CREATE TRIGGER item_count
AFTER INSERT ON orders
FOR EACH ROW
-- Edit Trigger body below
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END $$
DELIMITER ;
