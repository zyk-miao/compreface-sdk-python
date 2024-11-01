import aiofiles

from .base_service import BaseService, AsyncBaseService
from .server_api_list import DETECT_URL


class DetectionService(BaseService):
    def __init__(self, api_key: str, server_prefix: str):
        super().__init__(api_key, server_prefix)

    def detect(self, img_path: str, limit: int = 0, threshold: float = None, face_plugins: str = None,
               status: bool = False) -> str:
        with open(img_path, 'rb') as f:
            rv = self._client.post(f'{DETECT_URL}', params={
                'limit': limit,
                'threshold': threshold,
                'face_plugins': face_plugins,
                'status': status,
            }, files={'file': f})
            return rv.json()

    def detect_by_64(self, img64: str, limit: int = 0, threshold: float = None, face_plugins: str = None,
                     status: bool = False) -> str:
        rv = self._client.post(f'{DETECT_URL}', params={
            'limit': limit,
            'threshold': threshold,
            'face_plugins': face_plugins,
            'status': status,
        }, json={'file': img64})
        return rv.json()


class AsyncDetectionService(AsyncBaseService):
    def __init__(self, api_key: str, server_prefix: str):
        super().__init__(api_key, server_prefix)

    async def detect(self, img_path: str, limit: int = 0, threshold: float = None, face_plugins: str = None,
                     status: bool = False) -> str:
        async with  aiofiles.open(img_path, 'rb') as f:
            content=await f.read()
            rv = await self._client.post(f'{DETECT_URL}', params={
                'limit': limit,
                'threshold': threshold,
                'face_plugins': face_plugins,
                'status': status,
            }, files={'file': (f.name,content)})
            return rv.json()

    async def detect_by_64(self, img64: str, limit: int = 0, threshold: float = None, face_plugins: str = None,
                           status: bool = False) -> str:
        rv = await self._client.post(f'{DETECT_URL}', params={
            'limit': limit,
            'threshold': threshold,
            'face_plugins': face_plugins,
            'status': status,
        }, json={'file': img64})
        return rv.json()
