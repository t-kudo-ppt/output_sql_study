-- Table: company_master (企業マスタテーブル)

CREATE TABLE company_master (
    company_id int(10) NOT NULL PRI COMMENT '企業の一意識別子',
    company_name varchar(100) NOT NULL COMMENT '企業の名前',
    address varchar(255) COMMENT '企業の住所',
    phone_number varchar(20) COMMENT '企業の電話番号',
    email varchar(100) COMMENT '企業のメールアドレス',
    registration_date date COMMENT '企業の登録日',
    status varchar(20) COMMENT '企業のステータス',
    created_date date NOT NULL COMMENT 'レコードの作成日',
    created_by int(10) NOT NULL COMMENT 'レコードを作成したユーザーのID',
    updated_date date COMMENT 'レコードの最終更新日',
    updated_by int(10) COMMENT 'レコードを最後に更新したユーザーのID',
    deleted_date date COMMENT 'レコードの削除日',
    deleted_by int(10) COMMENT 'レコードを削除したユーザーのID',
    delete_flag char(1) COMMENT '削除フラグ（'0' は削除されていない、'1' は削除された）',
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
