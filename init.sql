-- データベースの文字セットをUTF-8に設定
CREATE DATABASE IF NOT EXISTS mydatabase
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_unicode_ci;

USE mydatabase;

-- テーブルの作成
CREATE TABLE company_master (
    company_id INT(10) NOT NULL AUTO_INCREMENT COMMENT '企業の一意識別子',
    company_name VARCHAR(100) NOT NULL COMMENT '企業の名前',
    address VARCHAR(255) COMMENT '企業の住所',
    phone_number VARCHAR(20) COMMENT '企業の電話番号',
    email VARCHAR(100) COMMENT '企業のメールアドレス',
    registration_date DATE COMMENT '企業の登録日',
    status VARCHAR(20) COMMENT '企業のステータス',
    created_date DATE NOT NULL COMMENT 'レコードの作成日',
    created_by INT(10) NOT NULL COMMENT 'レコードを作成したユーザーのID',
    updated_date DATE COMMENT 'レコードの最終更新日',
    updated_by INT(10) COMMENT 'レコードを最後に更新したユーザーのID',
    deleted_date DATE COMMENT 'レコードの削除日',
    deleted_by INT(10) COMMENT 'レコードを削除したユーザーのID',
    delete_flag CHAR(1) DEFAULT '0' COMMENT '削除フラグ（''0'' は削除されていない、''1'' は削除された）',
    PRIMARY KEY (company_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='企業マスタ';

CREATE TABLE company_user_master (
    user_id INT(10) NOT NULL AUTO_INCREMENT COMMENT 'ユーザーの一意識別子',
    company_id INT(10) NOT NULL COMMENT 'ユーザーが所属する企業のID',
    first_name VARCHAR(50) COMMENT 'ユーザーの名',
    last_name VARCHAR(50) COMMENT 'ユーザーの姓',
    email VARCHAR(100) COMMENT 'ユーザーのメールアドレス',
    phone_number VARCHAR(20) COMMENT 'ユーザーの電話番号',
    position VARCHAR(50) COMMENT 'ユーザーの役職',
    department VARCHAR(50) COMMENT 'ユーザーの部署',
    start_date DATE COMMENT 'ユーザーの入社日',
    status VARCHAR(20) COMMENT 'ユーザーのステータス',
    created_date DATE NOT NULL COMMENT 'レコードの作成日',
    created_by INT(10) NOT NULL COMMENT 'レコードを作成したユーザーのID',
    updated_date DATE COMMENT 'レコードの最終更新日',
    updated_by INT(10) COMMENT 'レコードを最後に更新したユーザーのID',
    deleted_date DATE COMMENT 'レコードの削除日',
    deleted_by INT(10) COMMENT 'レコードを削除したユーザーのID',
    delete_flag CHAR(1) DEFAULT '0' COMMENT '削除フラグ（''0'' は削除されていない、''1'' は削除された）',
    PRIMARY KEY (user_id),
    CONSTRAINT fk_company_user_master_company_id FOREIGN KEY (company_id)
        REFERENCES company_master (company_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='企業ユーザーマスタ';

CREATE TABLE log_table (
    log_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'シーケンスキー',
    log_text TEXT COMMENT 'ログのテキスト',
    log_type CHAR(1) NOT NULL COMMENT 'ログの種類（Q: 質問, A: 回答）',
    created_date DATE NOT NULL COMMENT 'レコードの作成日',
    created_by INT(10) NOT NULL COMMENT 'レコードを作成したユーザーのID',
    updated_date DATE COMMENT 'レコードの最終更新日',
    updated_by INT(10) COMMENT 'レコードを最後に更新したユーザーのID',
    deleted_date DATE COMMENT 'レコードの削除日',
    deleted_by INT(10) COMMENT 'レコードを削除したユーザーのID',
    delete_flag CHAR(1) DEFAULT '0' COMMENT '削除フラグ（''0'' は削除されていない、''1'' は削除された）'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='ログ';
