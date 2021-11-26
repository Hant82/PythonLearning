-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 26, 2021 lúc 10:25 AM
-- Phiên bản máy phục vụ: 10.4.21-MariaDB
-- Phiên bản PHP: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `game_card`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `games`
--

CREATE TABLE `games` (
  `id` int(11) NOT NULL,
  `winner` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `route` int(11) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `games`
--

INSERT INTO `games` (`id`, `winner`, `route`, `date_time`) VALUES
(6, 'b', 1, '2021-11-24 19:40:54'),
(7, 'b', 2, '2021-11-24 19:41:15'),
(8, 'hân', 3, '2021-11-25 15:56:17'),
(9, 'Đức', 4, '2021-11-24 15:56:58');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `logs`
--

CREATE TABLE `logs` (
  `id` int(11) NOT NULL,
  `gamer` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `deck` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `point` int(11) NOT NULL,
  `biggest_card` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `route` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `logs`
--

INSERT INTO `logs` (`id`, `gamer`, `deck`, `point`, `biggest_card`, `route`) VALUES
(22, 'a', '8♥4♦2♣', 4, '4♦', 1),
(23, 'b', 'A♥6♣8♣', 5, 'A♥', 1),
(24, 'a', '4♠9♠5♠', 8, '9♠', 2),
(25, 'b', '7♠6♥5♥', 8, '6♥', 2),
(26, 'hà', '6♠9♠5♥', 0, '5♥', 3),
(27, 'hân', '3♦2♣4♠', 9, '3♦', 3),
(28, 'đức', '9♦6♣3♣', 8, '9♦', 3),
(29, 'Đức', '5♥7♦3♥', 5, '7♦', 4),
(30, 'Hà ', '8♥3♣4♦', 5, '4♦', 4),
(31, 'Hân', '5♦A♥5♣', 1, '5♦', 4),
(32, 'ab', 'A♦A♥6♥', 8, 'A♦', 5),
(33, 'cd', '3♠6♠4♥', 3, '4♥', 5),
(34, 'a', '6♣4♥8♣', 8, '4♥', 6),
(35, 'b', '5♠3♠6♦', 4, '6♦', 6);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `games`
--
ALTER TABLE `games`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `games`
--
ALTER TABLE `games`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT cho bảng `logs`
--
ALTER TABLE `logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
