"""
    name: weeks 
    once: false
    origin: tgpy://module/weeks
    priority: 1728301316
"""
async def count_parity(first_week: Union[int, None], week: int) -> Union[str, None]:
    if first_week is None:
        week_parity = None
    elif (week - first_week) % 2 == 0:
        week_parity = "odd"
    else:
        week_parity = "even"
    return week_parity


async def get_day(day: datetime):
    start_str = "02.09.2024"
    start_date = datetime.strptime(start_str, "%d.%m.%Y")
    first_week = start_date.isocalendar().week
    week = day.isocalendar().week
    week_parity = await count_parity(first_week, week)

    if week_parity == "even":
        result = "Чётная"
    elif week_parity == "odd":
        result = "Нечётная"
    else:
        result = "Неизвестно"
    return result


async def week_parity():
    return await get_day(datetime.now())

async def голубой_или_ещё_нет():
    if await week_parity() == "Чётная":
        return "Голубой (чётная)"
    elif await week_parity() == "Нечётная":
        return "Белый (нечётная)"
    else:
        return "Неизвестно"

