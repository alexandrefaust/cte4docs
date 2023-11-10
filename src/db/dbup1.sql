USE cte4docs;

CREATE TABLE IF NOT EXISTS `Energia` ( 
	`IDEnergia` VARCHAR(150) NOT NULL , 
	`IDConjunto` VARCHAR(100) NULL , 
	`IDEdificio` INT NULL ,
	`Concessionaria` DOUBLE NULL , 
	`Comentario` VARCHAR(500) NULL ,
	`DataAtivacao` DATETIME NULL ,
	`DataInativacao` DATETIME NULL ,
	`NumeroEquipamento` VARCHAR(200) NULL , 
	`Origem` DOUBLE NULL , 
	`PavimentoModulo` VARCHAR(100) NULL , 
	`Tipo` DOUBLE NULL ,
	PRIMARY KEY (IDEnergia)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `DadoEnergia` ( 
	`ID` INT NOT NULL AUTO_INCREMENT , 
	`IDEnergia` VARCHAR(150) NULL , 

    `Comentarios` VARCHAR(500) NULL , 
    `ComentariosAdicionais` VARCHAR(500) NULL , 

    `LocalData` VARCHAR(150) NULL , 
    `Periodo` VARCHAR(150) NULL, 

    `DataInicio` DATETIME NULL , 
    `DataFinal` DATETIME NULL , 
    `Dias` INT NULL , 

    `Status` VARCHAR(100) DEFAULT 'Recebido', 
    `StatusChecagem` VARCHAR(100) NULL , 

	`CustoMercadoLivreLongoPrazo` VARCHAR(100) NULL , 
	`CompraMercadoLivreLongoPrazo` VARCHAR(100) NULL , 

    `Vencimento` DATETIME NULL , 
	`IDDocumento` VARCHAR(100) NULL , 
	PRIMARY KEY (ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `HistoricoEnergia` ( 
	`ID` INT NOT NULL AUTO_INCREMENT ,
	`IDDadoEnergia` INT NOT NULL ,
	`Data` VARCHAR(150) NULL , 
	`Dias` VARCHAR(150) NULL , 
	PRIMARY KEY (`ID`),
    FOREIGN KEY (IDDadoEnergia) REFERENCES DadoEnergia(ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `ItemEnergia` ( 
	`ID` INT NOT NULL AUTO_INCREMENT ,
	`IDDadoEnergia` INT NULL ,
	`IDHistoricoEnergia` INT NULL ,
	`Nome` VARCHAR(150) NULL , 
	`Categoria` VARCHAR(150) NULL , 
	`Periodo` VARCHAR(150) NULL , 
	`Tarifa` VARCHAR(150) NULL , 
	`Custo` VARCHAR(150) NULL , 
	`MedidaFaturada` VARCHAR(150) NULL , 
	`Contratada` VARCHAR(150) NULL , 
	`Medida` VARCHAR(150) NULL ,
	PRIMARY KEY (`ID`),
    FOREIGN KEY (IDDadoEnergia) REFERENCES DadoEnergia(ID),
	FOREIGN KEY (IDHistoricoEnergia) REFERENCES HistoricoEnergia(ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Gas` ( 
	`IDGas` VARCHAR(150) NOT NULL , 
	`IDConjunto` VARCHAR(100) NULL , 
	`IDEdificio` INT NULL ,
	`Concessionaria` DOUBLE NULL , 
	`Comentario` VARCHAR(500) NULL ,
	`DataAtivacao` DATETIME NULL ,
	`DataInativacao` DATETIME NULL ,
	`NumeroEquipamento` VARCHAR(200) NULL , 
	`Origem` DOUBLE NULL , 
	`PavimentoModulo` VARCHAR(100) NULL , 
	`Tipo` DOUBLE NULL ,
	PRIMARY KEY (IDGas)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `DadoGas` ( 
	`ID` INT NOT NULL AUTO_INCREMENT , 
	`IDGas` VARCHAR(150) NULL , 

    `Comentarios` VARCHAR(500) NULL , 
    `ComentariosAdicionais` VARCHAR(500) NULL , 

    `Periodo` VARCHAR(150) NULL, 

    `DataInicio` DATETIME NULL , 
    `DataFinal` DATETIME NULL , 
    `Dias` INT NULL , 

    `Status` VARCHAR(100) DEFAULT 'Recebido', 
    `StatusChecagem` VARCHAR(100) NULL , 

	`NumeroNF` VARCHAR(150) NULL , 
	`Fornecedor` VARCHAR(150) NULL , 
	`ClasseTarifaria` VARCHAR(150) NULL , 
	`ValorTotal` VARCHAR(150) NULL , 
	
    `Vencimento` DATETIME NULL , 
	`IDDocumento` VARCHAR(100) NULL , 
	PRIMARY KEY (ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `HistoricoGas` ( 
	`ID` INT NOT NULL AUTO_INCREMENT ,
	`IDDadoGas` INT NOT NULL ,
	`Data` VARCHAR(150) NULL , 
	PRIMARY KEY (`ID`),
    FOREIGN KEY (IDDadoGas) REFERENCES DadoGas(ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `ItemGas` ( 
	`ID` INT NOT NULL AUTO_INCREMENT ,
	`IDDadoGas` INT NULL ,
	`IDHistoricoGas` INT NULL ,
	`Nome` VARCHAR(150) NULL , 
	`Categoria` VARCHAR(150) NULL , 
	`MedidorTipo` VARCHAR(150) NULL , 
	`MedidorNumero` VARCHAR(150) NULL , 
	`Tarifa` VARCHAR(150) NULL , 
	`Custo` VARCHAR(150) NULL , 
	`MedidaFaturada` VARCHAR(150) NULL , 
	`Medida` VARCHAR(150) NULL , 
	`Tributavel` VARCHAR(150) NULL ,
	PRIMARY KEY (`ID`),
    FOREIGN KEY (IDDadoGas) REFERENCES DadoGas(ID),
	FOREIGN KEY (IDHistoricoGas) REFERENCES HistoricoGas(ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `APIversion` ( 
	`ID` INT NOT NULL AUTO_INCREMENT , 
	`Version` varchar(150) NOT NULL ,
	PRIMARY KEY (`ID`)
) ENGINE = InnoDB;

Commit;

INSERT INTO cte4docs.APIversion(ID, Version) VALUES (1, 'Update 1 - Dados de Energia e Gas');

Commit;