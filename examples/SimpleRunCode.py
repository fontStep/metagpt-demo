
from metagpt.actions import Action
from metagpt.logs import logger
import subprocess


class SimpleRunCode(Action):
    
    name: str = "SimpleRunCode"
    
    async def run(self,code_text_message):
        logger.info(f"{self.name} is running...")
        code_text = code_text_message[-1].content
        logger.info(f"{code_text=}")
        result = subprocess.run(["python", "-c", code_text], capture_output=True, text=True)
        code_result = result.stdout
        logger.info(f"{code_result=}")
        return code_result
    