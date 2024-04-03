CREATE DATABASE IF NOT EXISTS cte4docs;

USE cte4docs;

CREATE TABLE IF NOT EXISTS `Cliente` ( 
	`ID` INT NOT NULL AUTO_INCREMENT , 
	`Nome` VARCHAR(250) NOT NULL ,
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (`ID`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Endereco` ( 
	`ID` INT NOT NULL AUTO_INCREMENT , 
	`Bairro` VARCHAR(250) NOT NULL ,
	`CEP` VARCHAR(250) NOT NULL ,
	`Cidade` VARCHAR(250) NOT NULL ,
	`Estado` VARCHAR(250) NOT NULL ,
	`Logradouro` VARCHAR(250) NOT NULL ,
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (`ID`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Edificio` ( 
	`IDEdificio` VARCHAR(150) NOT NULL,
    `IDCliente` INT NULL , 
    `IDEndereco` INT NULL , 
	`AreaConstruida` DOUBLE NULL , 
	`AreaLocavel` DOUBLE NULL , 
	`CNPJ` VARCHAR(20) NOT NULL , 
	`Fundo` VARCHAR(100) NULL , 
	`GrossAssetValue` DOUBLE NULL , 
	`Nome` VARCHAR(250) NULL , 
	`Ownership` VARCHAR(100) NULL , 
    `StatusOperacao` VARCHAR(100) NULL , 
	`StatusPortfolio` VARCHAR(100) NULL , 
	`Tipologia` VARCHAR(150) NULL , 	
	`TipoOcupacao` VARCHAR(100) NULL , 
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (IDEdificio),
    FOREIGN KEY (IDCliente) REFERENCES Cliente(ID),
    FOREIGN KEY (IDEndereco) REFERENCES Endereco(ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Agua` ( 
	`IDAgua` VARCHAR(150) NOT NULL , 
	`IDConjunto` VARCHAR(100) NULL , 
	`IDEdificio` INT NULL ,
	`Concessionaria` DOUBLE NULL , 
	`Comentario` VARCHAR(500) NULL ,
	`DataAtivacao` DATETIME NULL ,
	`DataInativacao` DATETIME NULL ,
	`NumeroHidrometro` VARCHAR(200) NULL , 
	`Origem` DOUBLE NULL , 
	`PavimentoModulo` VARCHAR(100) NULL , 
	`Tipo` DOUBLE NULL ,
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (IDAgua)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `DadoAgua` ( 
	`ID` INT NOT NULL AUTO_INCREMENT , 
	`IDAgua` VARCHAR(150) NULL , 

    `Comentarios` VARCHAR(500) NULL , 
    `ComentariosAdicionais` VARCHAR(500) NULL , 

    `ConsumoEfetivo` INT NULL , 
    `ConsumoFaturado` INT NULL , 

    `Custo` DOUBLE NULL , 
    `CustoReais` DOUBLE NULL , 

    `DataInicio` DATETIME NULL , 
    `DataFinal` DATETIME NULL , 
    `Dias` INT NULL , 

    `ICMS` DOUBLE NULL , 
    `ICMSTaxa` DOUBLE NULL , 
    `ICMSValorFinal` DOUBLE NULL , 
	
	`PIS` DOUBLE NULL , 
    `PISTaxa` DOUBLE NULL , 
    `PISValorFinal` DOUBLE NULL ,

	`COFINS` DOUBLE NULL , 
    `COFINSTaxa` DOUBLE NULL , 
    `COFINSValorFinal` DOUBLE NULL ,

	`PISCOFINS` DOUBLE NULL , 
    `PISCOFINSTaxa` DOUBLE NULL , 
    `PISCOFINSValorFinal` DOUBLE NULL ,

    `LeituraAnterior` INT NULL , 
    `LeituraAtual` INT NULL , 

    `Periodo` VARCHAR(100) NULL , 

    `Status` VARCHAR(100) DEFAULT 'Recebido', 
    `StatusChecagem` VARCHAR(100) NULL , 

    `Vencimento` DATETIME NULL , 
	`TipoFaturamento` VARCHAR(150) NULL , 
	`IDDocumento` VARCHAR(100) NULL , 

	`NumeroNF` VARCHAR(150) NULL , 
	`Date` DATETIME NOT NULL DEFAULT NOW(),

	PRIMARY KEY (ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `IntervaloConsumo` ( 
	`ID` INT NOT NULL AUTO_INCREMENT ,
	`IDDadoAgua` INT NOT NULL ,
	`Intervalo` VARCHAR(100) NULL , 
	`ConsumoFaturado` DOUBLE NULL , 
	`CustoFaturado` DOUBLE NULL ,
	`Taxa` DOUBLE NULL ,
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (`ID`),
    FOREIGN KEY (IDDadoAgua) REFERENCES DadoAgua(ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Historico` ( 
	`ID` INT NOT NULL AUTO_INCREMENT ,
	`IDDadoAgua` INT NOT NULL ,
	`Data` VARCHAR(150) NULL , 
	`Dias` VARCHAR(150) NULL , 
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (`ID`),
    FOREIGN KEY (IDDadoAgua) REFERENCES DadoAgua(ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `ItemAgua` ( 
	`ID` INT NOT NULL AUTO_INCREMENT ,
	`IDDadoAgua` INT NULL ,
	`IDHistorico` INT NULL ,
	`Nome` VARCHAR(150) NULL , 
	`Categoria` VARCHAR(150) NULL , 
	`Valor` VARCHAR(150) NULL ,
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (`ID`),
    FOREIGN KEY (IDDadoAgua) REFERENCES DadoAgua(ID),
	FOREIGN KEY (IDHistorico) REFERENCES Historico(ID)
) ENGINE = InnoDB;

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
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (IDEnergia)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `DadoEnergia`(
	`ID` INT NOT NULL AUTO_INCREMENT,
	`IDEnergia` VARCHAR(150) NULL,

	`BandeiraTarifaria` VARCHAR(150) NULL,

    `Comentarios` VARCHAR(500) NULL,
    `ComentariosAdicionais` VARCHAR(500) NULL,

    `LocalData` VARCHAR(150) NULL, 
    `Periodo` VARCHAR(150) NULL, 

    `DataInicio` DATETIME NULL,
	`DataFinal` DATETIME NULL,
    `Dias` INT NULL,

    `Status` VARCHAR(100) DEFAULT 'Recebido', 
    `StatusChecagem` VARCHAR(100) NULL , 

	`CustoMercadoLivreLongoPrazo` VARCHAR(100) NULL,
	`CompraMercadoLivreLongoPrazo` VARCHAR(100) NULL,

    `Vencimento` DATETIME NULL,
	`IDDocumento` VARCHAR(100) NULL,

	`NumeroNF` VARCHAR(150) NULL,
	`Date` DATETIME NOT NULL DEFAULT NOW(),

	PRIMARY KEY (ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `HistoricoEnergia` ( 
	`ID` INT NOT NULL AUTO_INCREMENT ,
	`IDDadoEnergia` INT NOT NULL ,
	`Data` VARCHAR(150) NULL , 
	`Dias` VARCHAR(150) NULL , 
	`Date` DATETIME NOT NULL DEFAULT NOW(),
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
	`Date` DATETIME NOT NULL DEFAULT NOW(),
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
	`Date` DATETIME NOT NULL DEFAULT NOW(),
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
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `HistoricoGas` ( 
	`ID` INT NOT NULL AUTO_INCREMENT ,
	`IDDadoGas` INT NOT NULL ,
	`Data` VARCHAR(150) NULL , 
	`Date` DATETIME NOT NULL DEFAULT NOW(),
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
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (`ID`),
    FOREIGN KEY (IDDadoGas) REFERENCES DadoGas(ID),
	FOREIGN KEY (IDHistoricoGas) REFERENCES HistoricoGas(ID)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `APIversion` ( 
	`ID` INT NOT NULL AUTO_INCREMENT , 
	`Version` varchar(150) NOT NULL ,
	`Date` DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (`ID`)
) ENGINE = InnoDB;

Commit;

INSERT INTO cte4docs.APIversion(ID, Version) VALUES (1, 'Initial creation');

Commit;