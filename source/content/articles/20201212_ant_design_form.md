Title: Ant Design: Form
Author: mkostyrko
Date: 2020-12-12 10:00
Updated:
Category: react
Tags: react
Slug: react-antd
related_posts: 


![antd-logo](https://miro.medium.com/max/1000/1*fyrm-nSWAyxa5_m78mTq2g.png)

## >>[Wstępny zarys/szkielet]<<

### Tworzenie projektu przy pomocy CRA + instalacja ANTD

Ant Design jest biblioteką do stylowania komponentów Reactowych (współpracuje również z VUE oraz Angularem (NG-ZORRO)) utrzymywana przez Grupę Alibaba

Stworzenie projektu

    npx create-react-app antd_form

Dodanie zależności -> antd

    npm add antd

Zaimportowanie do App.js odpowiedniego komponentu oraz CSS do App.css

    // App.css - dodanie 1 linijki treści na samej górze
    @import '~antd/dist/antd.css';
    [...]

Zaimportowanie komponentu oraz jego zastosowanie

    //App.js
    import { Button } from 'antd';
    import './App.css';

    function App() {
      return (
        <div>
          <Button type="primary">Button</Button>
        </div>
      );
    }

    export default App;

---
### ANT DESIGN PRO

*ANT DESIGN PRO* jest biblioteką UI należącą do ANT DESIGN reklamującą się jako rozwiązanie dla projektów komercyjnych (przedsiębiorczych/enterprise), ale z dalszego jej opisu możemy się dowiedzieć, że została stworzona pod kątem interfejsów adminowskich.


---
### Pozycjonowanie elementów
#### Siatka - Grid

System/Pole jest podzielony na 24 sekcje/kolumny (nazwane 'box')

1 - należy zdefiniować zestaw kolumn oraz zdefiniować rząd:

      <Row>
          <Col span={12}>col-12</Col>
          <Col span={12}>col-12</Col>
      </Row>

2 - siatka/grid jest oparta o `display: flex`

3 - istnieje możliwość zdefiniowania odstępów/gutter -> `<Row gutter={16}>`

4 - offset/odsunięcie również jest definiowane w nawiązaniu do sekcji/kolumn `<Col span={8} offset={8}>`

5 - Nawiązując (parafrazując) do właściwości flexboxa istnieje możliwość ułożenie "dzieci" w poziomie wykorzystując właściwość `align`


    <Row justify="start"> / <Row justify="space-between"> / <Row justify="center">
          <Col span={4}>col-4</Col>
          <Col span={4}>col-4</Col>
    </Row>

6- ułożenie dzieci w pionie wykorzystuje właściwość `align`

    <Row justify="space-around" align="middle">
          <Col span={4}>
          </Col>
    </Row>

7 - istnieje możliwość wypełnienie całości stosując właściwość `flex` oraz definiowania relacji pomiędzy obiektami

    <Row>
          <Col flex={2}>2 / 5</Col>
          <Col flex={3}>3 / 5</Col>
    </Row>

8 - można również wykorzystać wartości znane z `bootstrapa`

<p class="codepen" data-height="465" data-theme-id="light" data-default-tab="js,result" data-user="mkostyrko" data-slug-hash="abmZPzZ" style="height: 465px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="Playground - antd@4.9">
  <span>See the Pen <a href="https://codepen.io/mkostyrko/pen/abmZPzZ">
  Playground - antd@4.9</a> by Mikołaj Kostyrko (<a href="https://codepen.io/mkostyrko">@mkostyrko</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>






---

Źródła:


[Ant Design - Form](https://ant.design/components/form/)

[SO - Correctly creating an antd Form using the extends React.Component mechanism](https://stackoverflow.com/questions/41181573/correctly-creating-an-antd-form-using-the-extends-react-component-mechanism)

[Code with Bibek - React Ant Design Project - Tech Website](https://www.youtube.com/playlist?list=PLiUrl-SQRR7LM5cw7azA2H_FZwFx2UgkI)


[Redux Form + antd](https://codesandbox.io/s/jzyl70wpk?file=/index.js)

[Use Form of Ant Design V4 in React Hooks](https://annacoding.com/article/7jDz3vvi3VdtYXYkvYpUp2/Use-Form-of-Ant-Design-V4-in-React-Hooks)

[Chinese Material Design This Chinese Design Language will Make You Want to Switch.](https://uxdesign.cc/chinese-material-design-5d31359df4a6)


YT

[Coding the World - 1 - Getting Started - Building a Contact Management System With React and Ant Design Library](https://www.youtube.com/watch?v=FizDLRlE6NE&t=777s&ab_channel=CodingTheWorld)

[Code with Bibek - React Ant Design Project - Tech Website](https://www.youtube.com/playlist?list=PLiUrl-SQRR7LM5cw7azA2H_FZwFx2UgkI)

