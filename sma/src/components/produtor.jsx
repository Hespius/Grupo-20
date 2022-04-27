import React, { Component } from "react";
import { connect } from "react-redux";
import DataGrid, {
  Column,
  Editing,
  Popup,
  Paging,
  Lookup,
  Form,
} from "devextreme-react/data-grid";
import "devextreme-react/text-area";
import { Item } from "devextreme-react/form";
import {
  setProduto,
  getOfertas,
  getCommodities,
} from "../middleware/servicesProduto";
import Navbar from "./navbar";

const data = [
  {
    id: 1,
    commodity: "soja",
    data_disponivel: new Date(),
    quantidade: 10,
    preco: 90,
  },
];

class Produtor extends Component {
  state = {
    cadastro_venda: {
      commodity: "",
      data_disponivel: "",
      quantidade: 0,
      preco: 0,
    },
  };
  handleSubmit = (e) => {
    e.preventDefault();
    console.log("submit");
  };

  onInsertHandler = async (ev) => {
    console.log(ev.data);
    const data = {
      commodity: ev.data.commodity,
      preco: ev.data.preco,
      quantidade: ev.data.quantidade,
      data_disponivel: ev.data.data_disponivel,
    };
    console.log(data);
    var response = await setProduto(data, this.props.id, 1);
    console.log(response);
  };

  getData = async () => {
    var commodities = await getCommodities();
    var ofertas = await getOfertas({ produtorId: this.props.id });
    this.setState({
      ofertas: ofertas.data,
      commodities: commodities.data.map((x) => x.nome),
    });
  };

  componentDidMount() {
    // this.getOfertas();
    // this.getCommodities();
    this.getData();
  }

  render() {
    const { commodities } = this.state;
    return (
      <>
        <Navbar />
        <div className="std-div">
          <h1>Perfil do Produtor</h1>
          <DataGrid
            dataSource={this.state.ofertas}
            onRowInserting={this.onInsertHandler}
          >
            <Paging enabled={false} />
            <Editing
              mode="popup"
              allowAdding={true}
              allowUpdating={true}
              allowDeleting={true}
            >
              {/* <Popup title='Registrar' showTitle={true} width={700} height={500} /> */}
              <Column dataField="data_disponivel" dataType="date"></Column>
              <Column dataField="commodity">
                <Lookup
                  dataSource={commodities}
                  displayExpr="commodity"
                  valueExpr="commodity"
                  allowClearing={true}
                ></Lookup>
              </Column>
              {/* <Form>
                                <Item dataField = 'commodity'/>
                                <Item dataField = 'data_disponivel' dataType='date'/>
                                <Item dataField = 'quantidade' />
                                <Item dataField = 'preco' />

                            </Form> */}
            </Editing>
          </DataGrid>
        </div>
      </>
    );
  }
}

const mapStateToProps = (state) => ({
  nome: state.AutenticationReducer.nome,
  email: state.AutenticationReducer.email,
  id: state.AutenticationReducer.id,
});

export default connect(mapStateToProps, {})(Produtor);
