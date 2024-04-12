import duckdb
from git_logger.git_history import GitLogger

# appoint = iterate_file_versions(
#     repo_path="../md-appoint",
#     filepath='../md-appoint/availability.json',
#     show_progress=True
# )

# hq_outages = iterate_file_versions(
#     repo_path="../hq-outages",
#     filepath='../hq-outages/outages.json',
#     show_progress=True
# )

# iv = iterate_file_versions(
#     repo_path="../options-vol-data",
#     filepath='../options-vol-data/iv.csv',
#     show_progress=True
# )


git_logger = GitLogger(
    db_name="md-appoint.duckdb",
    table_name="app",
    filepath='../md-appoint/availability.json',
    repo_path="../md-appoint",
    data_type="json"
)
git_logger.log_git_history()
git_logger.con.execute("select exists(select * from information_schema.tables where table_name = 'app')").fetchone()[0]

with duckdb.connect("md-appoint.duckdb") as con:
    con.sql("select * from app").show()