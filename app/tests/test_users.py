import pytest
from httpx import AsyncClient

from fastapi import status

from .contants import (
    PREFIX,
    USER_CREATE_VALID,
    USER_CREATE_SUPERUSER_VERIFIED,
)


@pytest.mark.anyio
async def test_create_user(async_client: AsyncClient):
    resp = await async_client.request(
        method='POST',
        url=f'{PREFIX}/auth/register',
        json=USER_CREATE_VALID.model_dump(),
    )
    assert resp.status_code == status.HTTP_201_CREATED
    resp_data = resp.json()
    assert resp_data['email'] == USER_CREATE_VALID.email
    assert resp_data['is_active']
    assert not resp_data['is_superuser']
    assert not resp_data['is_verified']


@pytest.mark.anyio
async def test_create_superuser_invalid(async_client: AsyncClient):
    resp = await async_client.request(
        method='POST',
        url=f'{PREFIX}/auth/register',
        json=USER_CREATE_SUPERUSER_VERIFIED.model_dump(),
    )
    assert resp.status_code == status.HTTP_201_CREATED
    resp_data = resp.json()
    assert resp_data['email'] == USER_CREATE_SUPERUSER_VERIFIED.email
    assert resp_data['is_active']
    assert not resp_data['is_superuser']
    assert not resp_data['is_verified']
