"""
Core модуль приложения.
Содержит логику воспроизведения(Player) и извлечения данных из YouTube(YouTubeExtractor).
"""

from .player import Player
from .youtube import YouTubeExtractor

__all__ = [
    'Player',
    'YouTubeExtractor',
]