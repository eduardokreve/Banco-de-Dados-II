//Criação das tabelas

CREATE TABLE pagerevision(name VARCHAR, date DATE, author VARCHAR, text TEXT);

CREATE TABLE pageaudit(name VARCHAR, date DATE, dif_len INT, evento INT);


//Criação da função

CREATE OR REPLACE FUNCTION process_audit() RETURNS TRIGGER
    AS $$  
    DECLARE
    diferenca INTEGER := 0;

    BEGIN
    	IF (TG_OP = 'DELETE') THEN
            diferenca := CHAR_LENGTH(old.text) * -1;

			INSERT into pageaudit VALUES (old.name, now(), diferenca, 3);
			RETURN OLD;
		ELSIF (TG_OP = 'UPDATE') THEN
            diferenca := CHAR_LENGTH(new.text) - CHAR_LENGTH(old.text);
            
            INSERT into pageaudit VALUES (new.name, now(), diferenca, 2);
			RETURN NEW;
		ELSIF (TG_OP = 'INSERT') THEN
            diferenca := CHAR_LENGTH(new.text);

            INSERT into pageaudit VALUES (new.name, now(), diferenca, 1);
			RETURN NEW;
		END IF;
		RETURN NULL;
   END;
$$ LANGUAGE plpgsql;


//Criação do Trigger

CREATE TRIGGER page_audit
AFTER INSERT OR UPDATE OR DELETE ON pagerevision
FOR EACH ROW EXECUTE PROCEDURE process_audit();