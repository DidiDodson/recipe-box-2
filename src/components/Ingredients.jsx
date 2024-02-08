import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid } from '@mui/x-data-grid';

export default function Ingredients( { ingredients } ) {
    const columns = [
        { field: 'id', headerName: 'ID', width: 70 },
        { field: 'name', headerName: 'Name', width: 130 },
        { field: 'category', headerName: 'Category', width: 130 }
    ];

    const rows = ingredients.map((row) => {
        return {
            id: row.id,
            name: row.name,
            category: row.category
        }
    })
      
    return (
        <div>
            <div margin="50px">
                <h1 margin='20px'>Ingredients</h1>
            </div>
           

            <Box sx={{ height: 400, width: '70%', padding: '20px' }}>
                {ingredients && ingredients.length > 0 && (
                    <DataGrid
                        rows={rows.sort((a, b) => a.id - b.id)}
                        columns={columns}
                        initialState={{
                            pagination: {
                              paginationModel: {
                                pageSize: 5,
                              },
                            },
                          }}
                    />
                )}
            </Box>
        </div>
    );
}