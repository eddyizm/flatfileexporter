import logging
from tortoise import Tortoise
from typing import List, Optional, Tuple

from core.constants import PROD_SERVER

log = logging.getLogger()


class MSSQLConnectionPool:
    """Minimal MSSQL connection pool with Tortoise"""

    @staticmethod
    async def initialize(connection_string: str) -> None:
        """Call this once at startup"""
        await Tortoise.init(
            db_url=connection_string,
            modules={"models": ["models.payment_exception"]},
        )

    @classmethod
    async def send_dbmail(
        cls,
        recipients: List[str],
        subject: str,
        body: str,
        profile_name: str,
        body_format: str = "HTML",
        copy_recipients: Optional[List[str]] = None,
        blind_copy_recipients: Optional[List[str]] = None,
    ) -> Tuple[bool, Optional[str]]:
        """Async wrapper for sp_send_dbmail"""
        recipients_str = ";".join(recipients)
        cc_str = ";".join(copy_recipients) if copy_recipients else None
        bcc_str = ";".join(blind_copy_recipients) if blind_copy_recipients else None

        sql = """
        EXEC msdb.dbo.sp_send_dbmail
            @profile_name = ?,
            @recipients = ?,
            @subject = ?,
            @body = ?,
            @body_format = ?,
            @copy_recipients = ?,
            @blind_copy_recipients = ?;
        """

        params = [
            profile_name,
            recipients_str,
            subject,
            body,
            body_format,
            cc_str,
            bcc_str,
        ]

        try:
            await cls.execute_query(sql, params)
            return True, None
        except Exception as e:
            return False, f"Email error: {str(e)}"

    @staticmethod
    async def close() -> None:
        """Call this at shutdown"""
        await Tortoise.close_connections()

    @classmethod
    def get_prod_db_string(cls, database):
        log.info("connectiong to prod db")
        return f"mssql://@{PROD_SERVER}:1433/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

    @classmethod
    def get_local_db_string(cls):
        db_string = "mssql://sa:StrongPassw0rd!@localhost:1433/MockDB?driver=ODBC Driver 17 for SQL Server"
        log.info(db_string)
        return db_string
