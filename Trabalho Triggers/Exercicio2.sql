//Criação das tabelas

CREATE TABLE availableflights(num_flight INT, date DATE, numberoffreeseats INT,
price FLOAT);

CREATE TABLE bookings(num_flight INT, date DATE, passenger INT, price FLOAT);


//Criação da função

CREATE OR REPLACE FUNCTION lugares_livres_voos() RETURNS TRIGGER
	AS $$
	DECLARE
    verifica VARCHAR(2) := 'of';   
	assento INTEGER := 0;
    BEGIN
		IF (TG_OP = 'INSERT') THEN

			assento (SELECT * into strict numberoffreeseats from availableflight); /* erro nesta linha */

			IF (assento >= 1) THEN
				new.numberoffreeseats := old.numberoffreeseats - 1;
				verifica := 'ok';
				RETURN NEW;
			END IF;

			IF (verifica = 'ok') THEN
				new.price := old.price + 50;

				INSERT into availableflights values (new.num_flight, new.date,new.numberoffreeseats,new.price);
				RETURN NEW;
			ELSE 
				RAISE NOTICE 'Emissao do ticket falhou';
				RETURN NEW;
			END IF;
		END if;
		RETURN NULL;
   END;
$$ LANGUAGE plpgsql;

//Criação do Trigger

CREATE TRIGGER voos
AFTER INSERT ON bookings
FOR EACH ROW EXECUTE PROCEDURE lugares_livres_voos();

//Inserir o primeiro voo
insert into availableflights values (1, '2019/03/20',50,500);
