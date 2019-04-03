//Criação das tabelas

CREATE TABLE auditoria(empregado_id INT, cpf CHAR(12),
num_Departamento INTEGER, salario DECIMAL(10,2), supervisor VARCHAR(50),
evento INT, usuario VARCHAR, data DATE);

CREATE TABLE empregado(id INTEGER PRIMARY KEY, nome VARCHAR(50), cpf VARCHAR(15),
num_Departamento INTEGER, salario DECIMAL(10,2), supervisor varchar(50));


//Criação da função

CREATE OR REPLACE FUNCTION process_empregado_audit() RETURNS TRIGGER
    AS $$   
    BEGIN
    	IF (TG_OP = 'DELETE') THEN
			INSERT into auditoria VALUES (old.id, old.cpf, old.num_Departamento,
		old.salario, old.supervisor, 3, current_user, now());
			RETURN OLD;
		ELSIF (TG_OP = 'UPDATE') THEN
			INSERT into auditoria VALUES (new.id, new.cpf, new.num_Departamento,
		new.salario, new.supervisor, 2, current_user, now());
			RETURN NEW;
		ELSIF (TG_OP = 'INSERT') THEN
			INSERT into auditoria VALUES (new.id, new.cpf, new.num_Departamento,
		new.salario, new.supervisor, 1, current_user, now());
			RETURN NEW;
		END IF;
		RETURN NULL;
   END;
$$ LANGUAGE plpgsql;


//Criação do Trigger

CREATE TRIGGER empregado_audit
AFTER INSERT OR UPDATE OR DELETE ON empregado
FOR EACH ROW EXECUTE PROCEDURE process_empregado_audit();