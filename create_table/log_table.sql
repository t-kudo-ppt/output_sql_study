-- Table: log_table (ログテーブル)

CREATE TABLE log_table (
    log_id int(11) NOT NULL PRI COMMENT 'シーケンスキー',
    log_text text COMMENT 'ログのテキスト',
    log_type char(1) NOT NULL COMMENT 'ログの種類（Q: 質問, A: 回答）',
    created_date date NOT NULL COMMENT 'レコードの作成日',
    created_by int(10) NOT NULL COMMENT 'レコードを作成したユーザーのID',
    updated_date date COMMENT 'レコードの最終更新日',
    updated_by int(10) COMMENT 'レコードを最後に更新したユーザーのID',
    deleted_date date COMMENT 'レコードの削除日',
    deleted_by int(10) COMMENT 'レコードを削除したユーザーのID',
    delete_flag char(1) COMMENT '削除フラグ（'0' は削除されていない、'1' は削除された）',
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
