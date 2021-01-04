import pytest

from acachecontrol import AsyncCacheControl


@pytest.mark.asyncio
async def test_request(mocker):
    """Verify AsyncCacheControl.request works correctly."""
    mock_RCM = mocker.Mock()
    async with AsyncCacheControl(
        request_context_manager_cls=mock_RCM
    ) as cached_sess:
        _ = cached_sess.request("GET", "http://example.com")
        mock_RCM.assert_called_with(
            cached_sess._async_client_session,
            cached_sess.cache,
            "GET",
            "http://example.com",
        )

        _ = cached_sess.request(
            "POST", "http://example.com", data={"key": "value"}
        )
        mock_RCM.assert_called_with(
            cached_sess._async_client_session,
            cached_sess.cache,
            "POST",
            "http://example.com",
            data={"key": "value"},
        )


@pytest.mark.asyncio
async def test_get(mocker):
    """Verify AsyncCacheControl.get works correctly."""
    mock_RCM = mocker.Mock()
    async with AsyncCacheControl(
        request_context_manager_cls=mock_RCM
    ) as cached_sess:
        _ = cached_sess.get("http://example.com")
        mock_RCM.assert_called_with(
            cached_sess._async_client_session,
            cached_sess.cache,
            "GET",
            "http://example.com",
            allow_redirects=True,
        )


@pytest.mark.asyncio
async def test_post(mocker):
    """Verify AsyncCacheControl.post works correctly."""
    mock_RCM = mocker.Mock()
    async with AsyncCacheControl(
        request_context_manager_cls=mock_RCM
    ) as cached_sess:
        _ = cached_sess.post("http://example.com", data={"key": "value"})
        mock_RCM.assert_called_with(
            cached_sess._async_client_session,
            cached_sess.cache,
            "POST",
            "http://example.com",
            data={"key": "value"},
        )


@pytest.mark.asyncio
async def test_clear_cashe(mocker):
    """Verify AsyncCacheControl.clear_cache works correctly."""
    mock_RCM = mocker.Mock()
    mock_cache = mocker.Mock()
    async with AsyncCacheControl(
        request_context_manager_cls=mock_RCM, cache=mock_cache
    ) as cached_sess:
        cached_sess.clear_cache()
        mock_cache.clear_cache.assert_called_once()
