export const titles = {
    'bus-types': 'Типы автобусов',
    'buses': 'Автобусы',
    'routes': 'Маршруты',
    'drivers': 'Водители',
    'driver-assignments': 'Назначения водителей',
    'bus-statuses': 'Статусы автобусов'
}

export const namingFunctions = {
    'bus-types': async (data) => {
        return `${data.name} (число мест: ${data.capacity})`
    },
    'buses': async (data) => {
        return `${data.license_plate} ` +
                `(${await getForeignField('bus-types', data.bus_type, 'name')})`
    },
    'routes': async (data) => {
        return `${data.number} (${data.start_point} - ${data.end_point})`
    },
    'drivers': async (data) => {
        return `${data.full_name} ` +
               `(автобус: ${await getForeignField('buses', data.main_bus, 'license_plate')}, ` +
               `маршрут: ${await getForeignField('routes', data.main_route, 'number')})`
    },
    'driver-assignments': async (data) => {
        return `${await getForeignField('drivers', data.driver, 'full_name')} на ` +
                `${await getBusName(data.bus)} | ${data.date}`
    },
    'bus-statuses': async (data) => {
        return `${await getBusName(data.bus)} - ${data.status} | ${data.date}`
    }
}

async function getForeignObject(type, id) {
    try {
        const token = localStorage.getItem('auth_token');
        if (!token) return null

        const response = await fetch(`http://127.0.0.1:8000/bus-depot/${type}/${id}`, {
            method: 'GET',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
            }
        });

        const data = await response.json();
        return data;
    } catch {
        return null;
    }
}

async function getForeignField(type, id, field) {
    const data = await getForeignObject(type, id);
    if (!data) return id;
    return data[field];
}

async function getBusName(id) {
    const data = await getForeignObject('buses', id)
    if (!data) return id;
    return `${data.license_plate} (${await getForeignField('bus-types', data.bus_type, 'name')})`
}
