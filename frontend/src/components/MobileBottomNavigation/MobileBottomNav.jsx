import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'

import CustomBottomNavigation from './MobileBottomNav.styles'
import CustomBottomNavigationAction from './BottomNavigationAction.styles'

import {
    useMediaQuery, 
} from '@mui/material'
import { useTheme } from '@mui/material/styles'
import PersonIcon from '@mui/icons-material/Person'
import FavoriteIcon from '@mui/icons-material/Favorite'
import TextsmsIcon from '@mui/icons-material/Textsms'
import MenuIcon from '@mui/icons-material/Menu'
import HomeIcon from '@mui/icons-material/Home'

export default function MobileBottomNav() {
    const [value, setValue] = useState(0)
    const navigate = useNavigate()
    const theme = useTheme()
    const isMobile = useMediaQuery(theme.breakpoints.down('sm'))

    if (!isMobile) return null

    return (
        <CustomBottomNavigation value={value} onChange={(event, value) => {setValue(newValue)}} showLabels>

                <CustomBottomNavigationAction
                    label='Главная'
                    icon={<HomeIcon />}
                    onClick={()=>navigate('/')}
                />

                <CustomBottomNavigationAction
                    label='Избранное'
                    icon={<FavoriteIcon />}
                    onClick={()=>navigate('/')}
                />

                <CustomBottomNavigationAction
                    label='Мои объяв.'
                    icon={<MenuIcon />}
                    onClick={()=>navigate('/')}
                />

                <CustomBottomNavigationAction
                    label='Сообщения'
                    icon={<TextsmsIcon />}
                    onClick={()=>navigate('/')}
                />

                <CustomBottomNavigationAction
                    label='Профиль'
                    icon={<PersonIcon />}
                    onClick={() => navigate('/')}
                />

        </CustomBottomNavigation>
    )
}