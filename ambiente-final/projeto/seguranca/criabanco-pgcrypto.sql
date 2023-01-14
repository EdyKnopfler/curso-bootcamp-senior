CREATE TABLE aviso(
id serial PRIMARY KEY,
titulo bytea NOT NULL,
resumo bytea NOT NULL,
thumb bytea NOT NULL,
imagem bytea,
texto bytea NOT NULL,
data bytea NOT NULL
);

-- Só precisa rodar uma vez no banco:
create extension pgcrypto;

-- Esta variavel tem a public key:
set session my.var.pubkey = '-----BEGIN PGP PUBLIC KEY BLOCK-----

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
zwHwIZ4+JtdWD9bnQzu8Dk1mEsWmy/ZMMTfw
=Eh5O
-----END PGP PUBLIC KEY BLOCK-----';

insert into aviso (titulo,resumo,thumb,imagem,texto,data) 
    SELECT         pgp_pub_encrypt(val.titulo, keys.pubkey) As titulo,
                   pgp_pub_encrypt(val.resumo, keys.pubkey) as resumo,
                   pgp_pub_encrypt(val.thumb, keys.pubkey) as thumb,
                   pgp_pub_encrypt(val.imagem, keys.pubkey) as imagem,
                   pgp_pub_encrypt(val.texto, keys.pubkey) as texto,
                   pgp_pub_encrypt(val.data, keys.pubkey) as data
                   
    FROM (VALUES ('Atenção para o prazo de programação de férias!!!',
                           'O prazo de programação de férias, para quem quer sair no próximo mês, termina dia 5 deste mês.',
                           'thumb1.png',
                           'praia1.png',
                           'Se você está pensando em tirar férias no próximo mês (Outubro) é importante ficar atento e solicitar suas férias até o dia 5. Procure o seu Supervisor ou entre no link <a href="https://siscorp.xpto.rede/adm/ferias">de férias</a> e preencha o formulário.',
                           '2021-09-02 10:10:05-3')
    ) as val(titulo,resumo,thumb,imagem,texto,data)
    CROSS JOIN (SELECT dearmor(current_setting('my.var.pubkey')::text) As pubkey) As keys;


