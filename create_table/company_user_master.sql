-- Table: company_user_master (企業ユーザーマスタテーブル)

CREATE TABLE company_user_master (
    user_id int(10) NOT NULL PRI COMMENT 'ユーザーの一意識別子',
    company_id int(10) NOT NULL MUL COMMENT 'ユーザーが所属する企業のID',
    first_name varchar(50) COMMENT 'ユーザーの名',
    last_name varchar(50) COMMENT 'ユーザーの姓',
    email varchar(100) COMMENT 'ユーザーのメールアドレス',
    phone_number varchar(20) COMMENT 'ユーザーの電話番号',
    position varchar(50) COMMENT 'ユーザーの役職',
    department varchar(50) COMMENT 'ユーザーの部署',
    start_date date COMMENT 'ユーザーの入社日',
    status varchar(20) COMMENT 'ユーザーのステータス',
    created_date date NOT NULL COMMENT 'レコードの作成日',
    created_by int(10) NOT NULL COMMENT 'レコードを作成したユーザーのID',
    updated_date date COMMENT 'レコードの最終更新日',
    updated_by int(10) COMMENT 'レコードを最後に更新したユーザーのID',
    deleted_date date COMMENT 'レコードの削除日',
    deleted_by int(10) COMMENT 'レコードを削除したユーザーのID',
    delete_flag char(1) COMMENT '削除フラグ（'0' は削除されていない、'1' は削除された）',
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
