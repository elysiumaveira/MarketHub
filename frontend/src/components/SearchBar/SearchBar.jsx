import { useState, useEffect } from 'react'

import {
    useTheme,
    useMediaQuery,
    TextField,
    InputAdornment,
} from '@mui/material'
import { SearchOutlined } from '@mui/icons-material'

export default function SearchBar({ placeholder = 'Поиск...', onSearch }) {
    const theme = useTheme()
        const isMobile = useMediaQuery(theme.breakpoints.down('sm'))
        const [searchTerm, setSearchTerm] = useState('')
        const handleSearch = (term) => {setSearchTerm(term)}

    return (
        <TextField 
            fullWidth
            variant='outlined'
            size='small'
            placeholder={placeholder}
            onChange={(e) => onSearch(e.target.value)}
            sx={{
                maxWidth: isMobile ? '100%' : '200%', 
                backgroundColor: '#f0f0f0', 
                borderRadius: '16px',
                '& .MuiOutlinedInput-notchedOutline': {border: 'none'},
            }}
            slotProps={{
                input: {
                    endAdornment: (
                        <InputAdornment position='end'>
                            <SearchOutlined />
                        </InputAdornment>
                    )
                }
            }}
        />
    )
}