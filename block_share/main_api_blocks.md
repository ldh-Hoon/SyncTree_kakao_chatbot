# 보험상담 kakao chatbot




### SyncTree 협업용

##### Blocks
<details>
    <summary>request - header </summary>

```XML
<block xmlns="https://developers.google.com/blockly/xml" type="collection_hashmap">
  <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
  <value name="ADD0">
    <block type="parameter_create">
      <value name="key">
        <block type="primitive_string">
          <field name="VALUE">Content-Type</field>
        </block>
      </value>
      <value name="value">
        <block type="miscellaneous_protocol_content_type">
          <field name="content-type">application/json</field>
        </block>
      </value>
      <value name="datatype">
        <block type="miscellaneous_parameter_type">
          <field name="parameter-type">string</field>
        </block>
      </value>
      <value name="description">
        <block type="primitive_string">
          <field name="VALUE">Content-Type</field>
        </block>
      </value>
      <value name="required">
        <block type="primitive_boolean">
          <field name="VALUE">true</field>
        </block>
      </value>
    </block>
  </value>
</block>

```

</details>

<details>
    <summary>request - body </summary>

```XML
<block xmlns="https://developers.google.com/blockly/xml" type="collection_hashmap">
  <mutation xmlns="http://www.w3.org/1999/xhtml" items="4"></mutation>
  <value name="ADD0">
    <block type="collection_pair">
      <value name="key">
        <block type="primitive_string">
          <field name="VALUE">intent</field>
        </block>
      </value>
      <value name="value">
        <block type="collection_hashmap">
          <mutation xmlns="http://www.w3.org/1999/xhtml" items="2"></mutation>
          <value name="ADD0">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">id</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_string">
                  <field name="VALUE">8bfw22kttmdm9ac13zahbrf3</field>
                </block>
              </value>
            </block>
          </value>
          <value name="ADD1">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">name</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_string">
                  <field name="VALUE">블록 이름</field>
                </block>
              </value>
            </block>
          </value>
        </block>
      </value>
    </block>
  </value>
  <value name="ADD1">
    <block type="collection_pair">
      <value name="key">
        <block type="primitive_string">
          <field name="VALUE">userRequest</field>
        </block>
      </value>
      <value name="value">
        <block type="collection_hashmap">
          <mutation xmlns="http://www.w3.org/1999/xhtml" items="7"></mutation>
          <value name="ADD0">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">callbackUrl</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_string">
                  <field name="VALUE">Asia/Seoul</field>
                </block>
              </value>
            </block>
          </value>
          <value name="ADD1">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">timezone</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_string">
                  <field name="VALUE">Asia/Seoul</field>
                </block>
              </value>
            </block>
          </value>
          <value name="ADD2">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">params</field>
                </block>
              </value>
              <value name="value">
                <block type="collection_hashmap">
                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                  <value name="ADD0">
                    <block type="collection_pair">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">ignoreMe</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">true</field>
                        </block>
                      </value>
                    </block>
                  </value>
                </block>
              </value>
            </block>
          </value>
          <value name="ADD3">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">block</field>
                </block>
              </value>
              <value name="value">
                <block type="collection_hashmap">
                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="2"></mutation>
                  <value name="ADD0">
                    <block type="collection_pair">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">id</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">8bfw22kttmdm9ac13zahbrf3</field>
                        </block>
                      </value>
                    </block>
                  </value>
                  <value name="ADD1">
                    <block type="collection_pair">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">name</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">블록 이름</field>
                        </block>
                      </value>
                    </block>
                  </value>
                </block>
              </value>
            </block>
          </value>
          <value name="ADD4">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">utterance</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_string">
                  <field name="VALUE">발화 내용</field>
                </block>
              </value>
            </block>
          </value>
          <value name="ADD5">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">lang</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_null"></block>
              </value>
            </block>
          </value>
          <value name="ADD6">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">user</field>
                </block>
              </value>
              <value name="value">
                <block type="collection_hashmap">
                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="3"></mutation>
                  <value name="ADD0">
                    <block type="collection_pair">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">id</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">608745</field>
                        </block>
                      </value>
                    </block>
                  </value>
                  <value name="ADD1">
                    <block type="collection_pair">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">type</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">accountId</field>
                        </block>
                      </value>
                    </block>
                  </value>
                  <value name="ADD2">
                    <block type="collection_pair">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">properties</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="collection_hashmap">
                          <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                        </block>
                      </value>
                    </block>
                  </value>
                </block>
              </value>
            </block>
          </value>
        </block>
      </value>
    </block>
  </value>
  <value name="ADD2">
    <block type="collection_pair">
      <value name="key">
        <block type="primitive_string">
          <field name="VALUE">bot</field>
        </block>
      </value>
      <value name="value">
        <block type="collection_hashmap">
          <mutation xmlns="http://www.w3.org/1999/xhtml" items="2"></mutation>
          <value name="ADD0">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">id</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_string">
                  <field name="VALUE">651e38c22ca7c359fca2769f</field>
                </block>
              </value>
            </block>
          </value>
          <value name="ADD1">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">name</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_string">
                  <field name="VALUE">봇 이름</field>
                </block>
              </value>
            </block>
          </value>
        </block>
      </value>
    </block>
  </value>
  <value name="ADD3">
    <block type="collection_pair">
      <value name="key">
        <block type="primitive_string">
          <field name="VALUE">action</field>
        </block>
      </value>
      <value name="value">
        <block type="collection_hashmap">
          <mutation xmlns="http://www.w3.org/1999/xhtml" items="5"></mutation>
          <value name="ADD0">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">name</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_string">
                  <field name="VALUE">5xtey9xghw</field>
                </block>
              </value>
            </block>
          </value>
          <value name="ADD1">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">clientExtra</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_null"></block>
              </value>
            </block>
          </value>
          <value name="ADD2">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">params</field>
                </block>
              </value>
              <value name="value">
                <block type="collection_hashmap">
                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                </block>
              </value>
            </block>
          </value>
          <value name="ADD3">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">id</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_string">
                  <field name="VALUE">m2i038homn143nn568cjzezm</field>
                </block>
              </value>
            </block>
          </value>
          <value name="ADD4">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">detailParams</field>
                </block>
              </value>
              <value name="value">
                <block type="collection_hashmap">
                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                </block>
              </value>
            </block>
          </value>
        </block>
      </value>
    </block>
  </value>
</block>

```

</details>

<details>
    <summary>statements - codeblock </summary>

```XML
<block xmlns="https://developers.google.com/blockly/xml" type="helper_code_section">
  <statement name="statements">
    <block type="helper_code_section">
      <statement name="statements">
        <block type="variable_create_set">
          <value name="variable_name">
            <block type="primitive_string">
              <field name="VALUE">req</field>
            </block>
          </value>
          <value name="variable_value">
            <block type="share_input">
              <value name="data">
                <block type="primitive_string">
                  <field name="VALUE">d49f62ec975292c9e6e809ac2653a5c2</field>
                </block>
              </value>
            </block>
          </value>
          <next>
            <block type="variable_create_set">
              <value name="variable_name">
                <block type="primitive_string">
                  <field name="VALUE">message</field>
                </block>
              </value>
              <value name="variable_value">
                <block type="collection_hashmap-get">
                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="4"></mutation>
                  <value name="array">
                    <block type="primitive_string">
                      <field name="VALUE">req</field>
                    </block>
                  </value>
                  <value name="ADD0">
                    <block type="primitive_string">
                      <field name="VALUE">request</field>
                    </block>
                  </value>
                  <value name="ADD1">
                    <block type="primitive_string">
                      <field name="VALUE">body</field>
                    </block>
                  </value>
                  <value name="ADD2">
                    <block type="primitive_string">
                      <field name="VALUE">userRequest</field>
                    </block>
                  </value>
                  <value name="ADD3">
                    <block type="primitive_string">
                      <field name="VALUE">utterance</field>
                    </block>
                  </value>
                </block>
              </value>
              <next>
                <block type="variable_create_set">
                  <value name="variable_name">
                    <block type="primitive_string">
                      <field name="VALUE">id</field>
                    </block>
                  </value>
                  <value name="variable_value">
                    <block type="collection_hashmap-get">
                      <mutation xmlns="http://www.w3.org/1999/xhtml" items="5"></mutation>
                      <value name="array">
                        <block type="primitive_string">
                          <field name="VALUE">req</field>
                        </block>
                      </value>
                      <value name="ADD0">
                        <block type="primitive_string">
                          <field name="VALUE">request</field>
                        </block>
                      </value>
                      <value name="ADD1">
                        <block type="primitive_string">
                          <field name="VALUE">body</field>
                        </block>
                      </value>
                      <value name="ADD2">
                        <block type="primitive_string">
                          <field name="VALUE">userRequest</field>
                        </block>
                      </value>
                      <value name="ADD3">
                        <block type="primitive_string">
                          <field name="VALUE">user</field>
                        </block>
                      </value>
                      <value name="ADD4">
                        <block type="primitive_string">
                          <field name="VALUE">id</field>
                        </block>
                      </value>
                    </block>
                  </value>
                  <next>
                    <block type="variable_create_set">
                      <value name="variable_name">
                        <block type="primitive_string">
                          <field name="VALUE">callbackUrl</field>
                        </block>
                      </value>
                      <value name="variable_value">
                        <block type="collection_hashmap-get">
                          <mutation xmlns="http://www.w3.org/1999/xhtml" items="4"></mutation>
                          <value name="array">
                            <block type="primitive_string">
                              <field name="VALUE">req</field>
                            </block>
                          </value>
                          <value name="ADD0">
                            <block type="primitive_string">
                              <field name="VALUE">request</field>
                            </block>
                          </value>
                          <value name="ADD1">
                            <block type="primitive_string">
                              <field name="VALUE">body</field>
                            </block>
                          </value>
                          <value name="ADD2">
                            <block type="primitive_string">
                              <field name="VALUE">userRequest</field>
                            </block>
                          </value>
                          <value name="ADD3">
                            <block type="primitive_string">
                              <field name="VALUE">callbackUrl</field>
                            </block>
                          </value>
                        </block>
                      </value>
                    </block>
                  </next>
                </block>
              </next>
            </block>
          </next>
        </block>
      </statement>
      <next>
        <block type="helper_code_section">
          <statement name="statements">
            <block type="block_store_package_block_1117_1234">
              <data>{"packageDetailId":1117,"blockDetailId":1234}</data>
              <value name="ID">
                <block type="primitive_string">
                  <field name="VALUE">d99b273035d35aa389b165cfa651173e</field>
                </block>
              </value>
              <value name="header">
                <block type="collection_hashmap">
                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                  <value name="ADD0">
                    <block type="parameter_create">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">Authorization</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">jI12jJhnjJia6tikiLcomhnmhnmhnmhnmhnmaxamEzmz</field>
                        </block>
                      </value>
                      <value name="datatype">
                        <block type="miscellaneous_parameter_type">
                          <field name="parameter-type">string</field>
                        </block>
                      </value>
                      <value name="description">
                        <block type="primitive_string">
                          <field name="VALUE">API Authorization Key (Default)</field>
                        </block>
                      </value>
                      <value name="required">
                        <block type="primitive_boolean">
                          <field name="VALUE">true</field>
                        </block>
                      </value>
                    </block>
                  </value>
                </block>
              </value>
              <value name="body">
                <block type="collection_hashmap">
                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="5"></mutation>
                  <value name="ADD0">
                    <block type="parameter_create">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">afonCd</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">0705</field>
                        </block>
                      </value>
                      <value name="datatype">
                        <block type="miscellaneous_parameter_type">
                          <field name="parameter-type">string</field>
                        </block>
                      </value>
                      <value name="description">
                        <block type="primitive_string">
                          <field name="VALUE">Affiliate Code</field>
                        </block>
                      </value>
                      <value name="required">
                        <block type="primitive_boolean">
                          <field name="VALUE">true</field>
                        </block>
                      </value>
                    </block>
                  </value>
                  <value name="ADD1">
                    <block type="parameter_create">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">reqRspnScCd</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">1</field>
                        </block>
                      </value>
                      <value name="datatype">
                        <block type="miscellaneous_parameter_type">
                          <field name="parameter-type">string</field>
                        </block>
                      </value>
                      <value name="description">
                        <block type="primitive_string">
                          <field name="VALUE">Request, response Identification code (Request : 1, Response : 2)</field>
                        </block>
                      </value>
                      <value name="required">
                        <block type="primitive_boolean">
                          <field name="VALUE">true</field>
                        </block>
                      </value>
                    </block>
                  </value>
                  <value name="ADD2">
                    <block type="parameter_create">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">svcId</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">OAE002A02</field>
                        </block>
                      </value>
                      <value name="datatype">
                        <block type="miscellaneous_parameter_type">
                          <field name="parameter-type">string</field>
                        </block>
                      </value>
                      <value name="description">
                        <block type="primitive_string">
                          <field name="VALUE">Service ID</field>
                        </block>
                      </value>
                      <value name="required">
                        <block type="primitive_boolean">
                          <field name="VALUE">true</field>
                        </block>
                      </value>
                    </block>
                  </value>
                  <value name="ADD3">
                    <block type="parameter_create">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">traDt</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">20230801180000</field>
                        </block>
                      </value>
                      <value name="datatype">
                        <block type="miscellaneous_parameter_type">
                          <field name="parameter-type">string</field>
                        </block>
                      </value>
                      <value name="description">
                        <block type="primitive_string">
                          <field name="VALUE">Transaction Date (YYYYMMDDHHMMSS)</field>
                        </block>
                      </value>
                      <value name="required">
                        <block type="primitive_boolean">
                          <field name="VALUE">true</field>
                        </block>
                      </value>
                    </block>
                  </value>
                  <value name="ADD4">
                    <block type="parameter_create">
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">traSrno</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">0000001</field>
                        </block>
                      </value>
                      <value name="datatype">
                        <block type="miscellaneous_parameter_type">
                          <field name="parameter-type">string</field>
                        </block>
                      </value>
                      <value name="description">
                        <block type="primitive_string">
                          <field name="VALUE">Transaction Serial Number</field>
                        </block>
                      </value>
                      <value name="required">
                        <block type="primitive_boolean">
                          <field name="VALUE">true</field>
                        </block>
                      </value>
                    </block>
                  </value>
                </block>
              </value>
            </block>
          </statement>
          <next>
            <block type="helper_code_section">
              <statement name="statements">
                <block type="variable_create_set">
                  <value name="variable_name">
                    <block type="primitive_string">
                      <field name="VALUE">kyobo_req</field>
                    </block>
                  </value>
                  <value name="variable_value">
                    <block type="share_input">
                      <value name="data">
                        <block type="primitive_string">
                          <field name="VALUE">d99b273035d35aa389b165cfa651173e</field>
                        </block>
                      </value>
                    </block>
                  </value>
                  <next>
                    <block type="variable_create_set">
                      <value name="variable_name">
                        <block type="primitive_string">
                          <field name="VALUE">kyobo_data</field>
                        </block>
                      </value>
                      <value name="variable_value">
                        <block type="collection_hashmap-get">
                          <mutation xmlns="http://www.w3.org/1999/xhtml" items="3"></mutation>
                          <value name="array">
                            <block type="primitive_string">
                              <field name="VALUE">kyobo_req</field>
                            </block>
                          </value>
                          <value name="ADD0">
                            <block type="primitive_string">
                              <field name="VALUE">response</field>
                            </block>
                          </value>
                          <value name="ADD1">
                            <block type="primitive_string">
                              <field name="VALUE">body</field>
                            </block>
                          </value>
                          <value name="ADD2">
                            <block type="primitive_string">
                              <field name="VALUE">goodList</field>
                            </block>
                          </value>
                        </block>
                      </value>
                      <next>
                        <block type="variable_create_set">
                          <value name="variable_name">
                            <block type="primitive_string">
                              <field name="VALUE">temp_list</field>
                            </block>
                          </value>
                          <value name="variable_value">
                            <block type="collection_arraylist">
                              <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                              <value name="ADD0">
                                <block type="primitive_string">
                                  <field name="VALUE"></field>
                                </block>
                              </value>
                            </block>
                          </value>
                          <next>
                            <block type="variable_create_set">
                              <value name="variable_name">
                                <block type="primitive_string">
                                  <field name="VALUE">need_add</field>
                                </block>
                              </value>
                              <value name="variable_value">
                                <block type="primitive_integer">
                                  <field name="VALUE">0</field>
                                </block>
                              </value>
                              <next>
                                <block type="variable_create_set">
                                  <value name="variable_name">
                                    <block type="primitive_string">
                                      <field name="VALUE">customer_data</field>
                                    </block>
                                  </value>
                                  <value name="variable_value">
                                    <block type="primitive_string">
                                      <field name="VALUE"></field>
                                    </block>
                                  </value>
                                </block>
                              </next>
                            </block>
                          </next>
                        </block>
                      </next>
                    </block>
                  </next>
                </block>
              </statement>
              <next>
                <block type="helper_code_section">
                  <statement name="statements">
                    <block type="loop_foreach">
                      <value name="element">
                        <block type="variable_get">
                          <value name="variable_name">
                            <block type="primitive_string">
                              <field name="VALUE">kyobo_data</field>
                            </block>
                          </value>
                        </block>
                      </value>
                      <value name="key">
                        <block type="primitive_string">
                          <field name="VALUE">key</field>
                        </block>
                      </value>
                      <value name="value">
                        <block type="primitive_string">
                          <field name="VALUE">value</field>
                        </block>
                      </value>
                      <statement name="statement">
                        <block type="variable_set">
                          <value name="variable_name">
                            <block type="primitive_string">
                              <field name="VALUE">need_add</field>
                            </block>
                          </value>
                          <value name="variable_value">
                            <block type="primitive_integer">
                              <field name="VALUE">1</field>
                            </block>
                          </value>
                          <next>
                            <block type="loop_foreach">
                              <value name="element">
                                <block type="variable_get">
                                  <value name="variable_name">
                                    <block type="primitive_string">
                                      <field name="VALUE">temp_list</field>
                                    </block>
                                  </value>
                                </block>
                              </value>
                              <value name="key">
                                <block type="primitive_string">
                                  <field name="VALUE">key2</field>
                                </block>
                              </value>
                              <value name="value">
                                <block type="primitive_string">
                                  <field name="VALUE">value2</field>
                                </block>
                              </value>
                              <statement name="statement">
                                <block type="logic_choice">
                                  <statement name="choice">
                                    <block type="logic_if">
                                      <mutation xmlns="http://www.w3.org/1999/xhtml" items="0"></mutation>
                                      <value name="expression">
                                        <block type="logic_expression-first">
                                          <value name="condition">
                                            <block type="logic_condition">
                                              <field name="compare">===</field>
                                              <value name="left_condition">
                                                <block type="is_string">
                                                  <value name="value">
                                                    <block type="variable_get">
                                                      <value name="variable_name">
                                                        <block type="primitive_string">
                                                          <field name="VALUE">value2</field>
                                                        </block>
                                                      </value>
                                                    </block>
                                                  </value>
                                                </block>
                                              </value>
                                              <value name="right_condition">
                                                <block type="primitive_boolean">
                                                  <field name="VALUE">true</field>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                        </block>
                                      </value>
                                      <statement name="statement">
                                        <block type="logic_if">
                                          <mutation xmlns="http://www.w3.org/1999/xhtml" items="0"></mutation>
                                          <value name="expression">
                                            <block type="logic_expression-first">
                                              <value name="condition">
                                                <block type="logic_condition">
                                                  <field name="compare">===</field>
                                                  <value name="left_condition">
                                                    <block type="common_util_handle_to_string">
                                                      <value name="value">
                                                        <block type="collection_hashmap-get">
                                                          <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                                          <value name="array">
                                                            <block type="primitive_string">
                                                              <field name="VALUE">value</field>
                                                            </block>
                                                          </value>
                                                          <value name="ADD0">
                                                            <block type="primitive_string">
                                                              <field name="VALUE">kcisGoodNm</field>
                                                            </block>
                                                          </value>
                                                        </block>
                                                      </value>
                                                    </block>
                                                  </value>
                                                  <value name="right_condition">
                                                    <block type="common_util_handle_to_string">
                                                      <value name="value">
                                                        <block type="variable_get">
                                                          <value name="variable_name">
                                                            <block type="primitive_string">
                                                              <field name="VALUE">value2</field>
                                                            </block>
                                                          </value>
                                                        </block>
                                                      </value>
                                                    </block>
                                                  </value>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                          <statement name="statement">
                                            <block type="variable_set">
                                              <value name="variable_name">
                                                <block type="primitive_string">
                                                  <field name="VALUE">need_add</field>
                                                </block>
                                              </value>
                                              <value name="variable_value">
                                                <block type="primitive_integer">
                                                  <field name="VALUE">0</field>
                                                </block>
                                              </value>
                                            </block>
                                          </statement>
                                        </block>
                                      </statement>
                                    </block>
                                  </statement>
                                </block>
                              </statement>
                              <next>
                                <block type="logic_choice">
                                  <statement name="choice">
                                    <block type="logic_if">
                                      <mutation xmlns="http://www.w3.org/1999/xhtml" items="0"></mutation>
                                      <value name="expression">
                                        <block type="logic_expression-first">
                                          <value name="condition">
                                            <block type="logic_condition">
                                              <field name="compare">===</field>
                                              <value name="left_condition">
                                                <block type="variable_get">
                                                  <value name="variable_name">
                                                    <block type="primitive_string">
                                                      <field name="VALUE">need_add</field>
                                                    </block>
                                                  </value>
                                                </block>
                                              </value>
                                              <value name="right_condition">
                                                <block type="primitive_integer">
                                                  <field name="VALUE">1</field>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                        </block>
                                      </value>
                                      <statement name="statement">
                                        <block type="collection_arraylist-add">
                                          <mutation xmlns="http://www.w3.org/1999/xhtml" items="0"></mutation>
                                          <value name="array">
                                            <block type="primitive_string">
                                              <field name="VALUE">temp_list</field>
                                            </block>
                                          </value>
                                          <value name="value">
                                            <block type="common_util_handle_to_string">
                                              <value name="value">
                                                <block type="collection_hashmap-get">
                                                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                                  <value name="array">
                                                    <block type="primitive_string">
                                                      <field name="VALUE">value</field>
                                                    </block>
                                                  </value>
                                                  <value name="ADD0">
                                                    <block type="primitive_string">
                                                      <field name="VALUE">kcisGoodNm</field>
                                                    </block>
                                                  </value>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                        </block>
                                      </statement>
                                    </block>
                                  </statement>
                                </block>
                              </next>
                            </block>
                          </next>
                        </block>
                      </statement>
                      <next>
                        <block type="loop_foreach">
                          <value name="element">
                            <block type="variable_get">
                              <value name="variable_name">
                                <block type="primitive_string">
                                  <field name="VALUE">temp_list</field>
                                </block>
                              </value>
                            </block>
                          </value>
                          <value name="key">
                            <block type="primitive_string">
                              <field name="VALUE">key</field>
                            </block>
                          </value>
                          <value name="value">
                            <block type="primitive_string">
                              <field name="VALUE">value</field>
                            </block>
                          </value>
                          <statement name="statement">
                            <block type="logic_choice">
                              <statement name="choice">
                                <block type="logic_if">
                                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="0"></mutation>
                                  <value name="expression">
                                    <block type="logic_expression-first">
                                      <value name="condition">
                                        <block type="logic_condition">
                                          <field name="compare">===</field>
                                          <value name="left_condition">
                                            <block type="variable_get">
                                              <value name="variable_name">
                                                <block type="primitive_string">
                                                  <field name="VALUE">key</field>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                          <value name="right_condition">
                                            <block type="primitive_integer">
                                              <field name="VALUE">0</field>
                                            </block>
                                          </value>
                                        </block>
                                      </value>
                                    </block>
                                  </value>
                                  <statement name="statement">
                                    <block type="variable_set">
                                      <value name="variable_name">
                                        <block type="primitive_string">
                                          <field name="VALUE">customer_data</field>
                                        </block>
                                      </value>
                                      <value name="variable_value">
                                        <block type="string_concat">
                                          <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                          <value name="target">
                                            <block type="variable_get">
                                              <value name="variable_name">
                                                <block type="primitive_string">
                                                  <field name="VALUE">customer_data</field>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                          <value name="ADD0">
                                            <block type="variable_get">
                                              <value name="variable_name">
                                                <block type="primitive_string">
                                                  <field name="VALUE">value</field>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                        </block>
                                      </value>
                                    </block>
                                  </statement>
                                  <next>
                                    <block type="logic_else">
                                      <statement name="statement">
                                        <block type="variable_set">
                                          <value name="variable_name">
                                            <block type="primitive_string">
                                              <field name="VALUE">customer_data</field>
                                            </block>
                                          </value>
                                          <value name="variable_value">
                                            <block type="string_concat">
                                              <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                              <value name="target">
                                                <block type="variable_get">
                                                  <value name="variable_name">
                                                    <block type="primitive_string">
                                                      <field name="VALUE">customer_data</field>
                                                    </block>
                                                  </value>
                                                </block>
                                              </value>
                                              <value name="ADD0">
                                                <block type="string_concat">
                                                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                                  <value name="target">
                                                    <block type="variable_get">
                                                      <value name="variable_name">
                                                        <block type="primitive_string">
                                                          <field name="VALUE">value</field>
                                                        </block>
                                                      </value>
                                                    </block>
                                                  </value>
                                                  <value name="ADD0">
                                                    <block type="primitive_string">
                                                      <field name="VALUE">,</field>
                                                    </block>
                                                  </value>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                        </block>
                                      </statement>
                                    </block>
                                  </next>
                                </block>
                              </statement>
                            </block>
                          </statement>
                        </block>
                      </next>
                    </block>
                  </statement>
                  <next>
                    <block type="helper_code_section">
                      <statement name="statements">
                        <block type="protocol_create">
                          <value name="unit">
                            <block type="protocol_unit_http_ssl">
                              <value name="method">
                                <block type="miscellaneous_protocol_method">
                                  <field name="method">post</field>
                                </block>
                              </value>
                              <value name="endPoint">
                                <block type="protocol_end_point_url">
                                  <value name="url">
                                    <block type="primitive_string">
                                      <field name="VALUE">https://ldhldh-langchain-kaka-api.hf.space/run/predict</field>
                                    </block>
                                  </value>
                                </block>
                              </value>
                              <value name="header">
                                <block type="collection_hashmap">
                                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                  <value name="ADD0">
                                    <block type="parameter_create">
                                      <value name="key">
                                        <block type="primitive_string">
                                          <field name="VALUE">Content-Type</field>
                                        </block>
                                      </value>
                                      <value name="value">
                                        <block type="miscellaneous_protocol_content_type">
                                          <field name="content-type">application/json</field>
                                        </block>
                                      </value>
                                      <value name="datatype">
                                        <block type="miscellaneous_parameter_type">
                                          <field name="parameter-type">string</field>
                                        </block>
                                      </value>
                                      <value name="description">
                                        <block type="primitive_string">
                                          <field name="VALUE">Content-Type</field>
                                        </block>
                                      </value>
                                      <value name="required">
                                        <block type="primitive_boolean">
                                          <field name="VALUE">true</field>
                                        </block>
                                      </value>
                                    </block>
                                  </value>
                                </block>
                              </value>
                              <value name="body">
                                <block type="collection_hashmap">
                                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                  <value name="ADD0">
                                    <block type="collection_pair">
                                      <value name="key">
                                        <block type="primitive_string">
                                          <field name="VALUE">data</field>
                                        </block>
                                      </value>
                                      <value name="value">
                                        <block type="collection_arraylist">
                                          <mutation xmlns="http://www.w3.org/1999/xhtml" items="4"></mutation>
                                          <value name="ADD0">
                                            <block type="variable_get">
                                              <value name="variable_name">
                                                <block type="primitive_string">
                                                  <field name="VALUE">message</field>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                          <value name="ADD1">
                                            <block type="variable_get">
                                              <value name="variable_name">
                                                <block type="primitive_string">
                                                  <field name="VALUE">id</field>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                          <value name="ADD2">
                                            <block type="variable_get">
                                              <value name="variable_name">
                                                <block type="primitive_string">
                                                  <field name="VALUE">customer_data</field>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                          <value name="ADD3">
                                            <block type="variable_get">
                                              <value name="variable_name">
                                                <block type="primitive_string">
                                                  <field name="VALUE">callbackUrl</field>
                                                </block>
                                              </value>
                                            </block>
                                          </value>
                                        </block>
                                      </value>
                                    </block>
                                  </value>
                                </block>
                              </value>
                              <statement name="options">
                                <block type="protocol_option_http_timeout">
                                  <value name="connect">
                                    <block type="primitive_integer">
                                      <field name="VALUE">2</field>
                                    </block>
                                  </value>
                                  <value name="max">
                                    <block type="primitive_integer">
                                      <field name="VALUE">2</field>
                                    </block>
                                  </value>
                                </block>
                              </statement>
                            </block>
                          </value>
                        </block>
                      </statement>
                    </block>
                  </next>
                </block>
              </next>
            </block>
          </next>
        </block>
      </next>
    </block>
  </statement>
</block>

```

</details>


<details>
    <summary>response context - body </summary>

```XML
<block xmlns="https://developers.google.com/blockly/xml" type="collection_hashmap">
  <mutation xmlns="http://www.w3.org/1999/xhtml" items="3"></mutation>
  <value name="ADD0">
    <block type="collection_pair">
      <value name="key">
        <block type="primitive_string">
          <field name="VALUE">version</field>
        </block>
      </value>
      <value name="value">
        <block type="primitive_string">
          <field name="VALUE">2.0</field>
        </block>
      </value>
    </block>
  </value>
  <value name="ADD1">
    <block type="collection_pair">
      <value name="key">
        <block type="primitive_string">
          <field name="VALUE">useCallback</field>
        </block>
      </value>
      <value name="value">
        <block type="primitive_boolean">
          <field name="VALUE">true</field>
        </block>
      </value>
    </block>
  </value>
  <value name="ADD2">
    <block type="collection_pair">
      <value name="key">
        <block type="primitive_string">
          <field name="VALUE">data</field>
        </block>
      </value>
      <value name="value">
        <block type="collection_hashmap">
          <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
          <value name="ADD0">
            <block type="collection_pair">
              <value name="key">
                <block type="primitive_string">
                  <field name="VALUE">text</field>
                </block>
              </value>
              <value name="value">
                <block type="primitive_string">
                  <field name="VALUE">서버 문제로 답변이 지연되고 있습니다...&#10;잠시만 기다려 주세요.</field>
                </block>
              </value>
            </block>
          </value>
        </block>
      </value>
    </block>
  </value>
</block>

```

</details>
