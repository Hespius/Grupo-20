import React, {Component} from 'react';

import DataGrid, {
  Column,
  Editing,
  Popup,
  Paging,
  Lookup,
  Form,
} from 'devextreme-react/data-grid';
import 'devextreme-react/text-area';
import { Item } from 'devextreme-react/form';


const data = [{
    id: 1,
    mercadoria: 'soja',
    disponibilidade: '2022/05/01',
    quantidade: 10,
    preco: 90,

}]

export default class Mercadorias extends Component {
    
    state = {
        cadastro_venda: {
        commodity: '',
        data_disponivel: '',
        quantidade: '',
        preco: 0,
    }
    }
    handleSubmit = (e) => {
        e.preventDefault()
        console.log('submit')
    }


    render() {

        return (

            <>
            <div className='std-div'>
            <h1>Perfil do Produtor</h1>
                <DataGrid
                    dataSource={data}>
                    <Paging enabled={false} />
                    <Editing
                        mode='popup'
                        allowAdding={true}
                        allowUpdating={true}
                        allowDeleting={true}>
                            <Popup title='Registrar' showTitle={true} width={700} height={500} />
                            <Form>
                                <Item dataField= 'mercadorias'/>
                                <Item dataField ='disponibilidade' />
                                <Item dataField = 'quantidade' />
                                <Item dataField = 'preco' />

                            </Form> 
                        </Editing>
                </DataGrid>
            </div>
            </>

        

        )
    }

}