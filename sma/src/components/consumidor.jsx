import React, { Component } from "react";
import Navbar from "./navbar";
import DataGrid, {
  Column,
  Editing,
  Popup,
  Paging,
  Lookup,
  Form,
  Item,
  Button,
  Selection,
} from "devextreme-react/data-grid";
import {
  Form as FormStd,
  SimpleItem,
  ButtonItem,
  GroupItem,
  SelectBox,
} from "devextreme-react/form";
import {
  Popup as StdPopup,
  Position,
  ToolbarItem,
  Item as PopupItem,
} from "devextreme-react/popup";

import {
  getCommodities,
  getOfertas,
  setOrdem,
} from "../middleware/servicesConsumidor";

// const commoditiesOptions = { items: ['Milho','Soja','Trigo'], searchEnabled: true, value: '' };
const statesOptions = {
  items: ["São Paulo", "Bahia", "Rio de Janeiro"],
  searchEnabled: true,
  value: "",
};

const popupButtonOptions = {
  text: "Comprar",
  width: 100,
};

const buttonOptions = {
  text: "Buscar",
  type: "success",
  useSubmitBehavior: true,
  width: 200,
};

export default class Consumidor extends Component {
  constructor(props) {
    super(props);
    this.navbar = React.createRef();
  }
  state = {
    busca_dados: {
      commodity: "",
      estado: "",
    },
    commoditiesOptions: {
      items: ["Milho", "Soja", "Trigo"],
      searchEnabled: true,
      value: "",
    },
    visiblePopup: false,
    quantidade: 0,
  };

  popupQtyOptions = {
    onDataFieldChange: this.handleQtyChange,
  };

  handleQtyChange = (e) => {
    console.log(e.value);
  };

  handleSubmit = async (e) => {
    e.preventDefault();
    console.log(e);
    console.log(this.state.busca_dados);
    await this.getOfertas(this.state.busca_dados.commodity);
  };

  handleChange = (e) => {
    const { busca_dados } = this.state;
    let newDados = busca_dados;

    console.log(e.value);

    newDados[e.dataField] = e.value;
    this.setState({ busca_dados: newDados });
  };

  handlePurchase = (e) => {
    console.log("Compra!");

    this.setState({ visiblePopup: true });

    console.log(this.state.visiblePopup);
  };

  handleHide = (e) => {
    console.log("Close!");

    this.setState({ visiblePopup: false });

    console.log(this.state.visiblePopup);
  };
  handleSelectionChange = (e) => {
    console.log("changed!");
  };

  onEditorPreparing = (event) => {
    // console.log(event)

    if (
      event.parentType === "dataRow" &&
      //   event.cells.column.dataField !== 'buttons' &&
      (event.dataField === "id" ||
        event.dataField === "commodity" ||
        event.dataField === "quantidade" ||
        event.dataField === "preco" ||
        event.dataField === "data_disponivel" ||
        event.dataField === "usuario")
    ) {
      event.editorOptions.disabled = true;
    }
  };

  handleRowPrepared = (e) => {
    console.log(e);
    const qtdeCompra = e.newData.comprar;
    const qtdeAtual = e.oldData.quantidade;

    if (qtdeCompra > qtdeAtual) {
      alert("valor > qtde disponível");
      return window.location.reload();
    } else {
      this.setState({ quantide: qtdeCompra });
      console.log("====== oldata =====", e.oldData);
      //   console.log("====== getUser ====", this.navbar.current.getUser());
      var ordemDto = {
        quantidade: qtdeCompra,
        data_requisitada: new Date(),
        comprador: 1,
        oferta: e.oldData.id,
      };
      console.log("===== ordemDTO =====", ordemDto);
      setOrdem(ordemDto);
    }
  };
  refreshDataGrid() {
    this.dataGrid.instance.refresh();
  }

  getOfertas = async (name) => {
    var result = await getOfertas({ commodityName: name });
    this.setState({ ofertas: result.data });
  };

  async componentDidMount() {
    var result = await getCommodities();
    console.log(result);
    this.setState({
      commoditiesOptions: {
        items: result.data.map((x) => x.commodity),
        searchEnabled: true,
        value: "",
      },
    });
  }

  render() {
    const { busca_dados, quantidade } = this.state.busca_dados;

    return (
      <>
        <Navbar />
        <div>
          <div className="std-div">
            <h1>Perfil do Consumidor</h1>
            <form onSubmit={this.handleSubmit}>
              <FormStd
                width={800}
                colCount={1}
                formData={busca_dados}
                onFieldDataChanged={this.handleChange}
              >
                <GroupItem caption="Busca" colCount={3}>
                  <SimpleItem
                    dataField="commodity"
                    editorType="dxSelectBox"
                    editorOptions={this.state.commoditiesOptions}
                  />
                  <SimpleItem
                    dataField="estado"
                    editorType="dxSelectBox"
                    editorOptions={statesOptions}
                  ></SimpleItem>
                  <ButtonItem buttonOptions={buttonOptions}></ButtonItem>
                </GroupItem>
              </FormStd>
            </form>
          </div>
        </div>
        <div className="std-div">
          <DataGrid
            dataSource={this.state.ofertas}
            ref={(ref) => (this.dataGrid = ref)}
            // defaultColumns={columns}
            rowAlternationEnabled={true}
            onSelectionChanged={this.handleSelectionChange}
            onEditorPreparing={this.onEditorPreparing}
            // onRowPrepared = {this.handleRowPrepared}
            onRowUpdating={this.handleRowPrepared}
          >
            {/* <Editing mode='popup' allowUpdating={true} useIcons={true}  /> */}
            <Paging enabled={false} />
            <Selection mode="multiple" />
            <Column dataField="usuario" />
            <Column dataField="commodity" />
            <Column dataField="data_disponivel" />
            <Column dataField="quantidade" caption="Qtde disponível" />
            <Column dataField="preco" />
            <Column dataField="comprar" allowEditing={true} />
            <Editing
              mode="popup"
              allowUpdating={true}
              useIcons={true}
              visible={false}
            >
              <Popup title="Compra" showTitle={true} width={700} height={300} />
            </Editing>

            {/* <Form>
                            <SelectBox dataField= 'commodity'/>
                            <Item dataField ='disponibilidade' />
                            <Item dataField = 'quantidade' />
                            <Item dataField = 'preco' />
                        </Form>  */}
          </DataGrid>
        </div>

        {/* <StdPopup
            visible={this.state.visiblePopup}
            onHiding={this.handleHide}
            showCloseButton={true}
            // closeOnOutsideClick={this.handleHide}
            showTitle={true}
            title='Compra'
            width={420}
            height={250}
            >
                
                <ToolbarItem text='Quantidade'
                toolbar="bottom"
                location="center"
                
                />
              
                <ToolbarItem widget='dxTextBox'
                toolbar="bottom"
                location="center"
                key='quantidade'
                options={this.popupQtyOptions}
                />
                <ToolbarItem widget='dxButton'
                options={popupButtonOptions}
                toolbar="bottom"
                location="center"/>

                <p>Preço: <span>{data[0].preco}</span></p>
                <p>Valor: <span>{data[0].preco * quantidade}</span></p>
                
            
        </StdPopup> */}
      </>
    );
  }
}
