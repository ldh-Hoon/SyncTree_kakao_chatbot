# 보험상담 kakao chatbot




### SyncTree 협업용 - kakao callback api

##### Blocks
<details>
    <summary>request - body </summary>

'''XML
<block xmlns="https://developers.google.com/blockly/xml" type="collection_hashmap">
  <mutation xmlns="http://www.w3.org/1999/xhtml" items="2"></mutation>
  <value name="ADD0">
    <block type="collection_pair">
      <value name="key">
        <block type="primitive_string">
          <field name="VALUE">url</field>
        </block>
      </value>
      <value name="value">
        <block type="primitive_string">
          <field name="VALUE">url</field>
        </block>
      </value>
    </block>
  </value>
  <value name="ADD1">
    <block type="collection_pair">
      <value name="key">
        <block type="primitive_string">
          <field name="VALUE">data</field>
        </block>
      </value>
      <value name="value">
        <block type="primitive_string">
          <field name="VALUE">data</field>
        </block>
      </value>
    </block>
  </value>
</block>
'''

</details>

<details>
    <summary>statements - codesection </summary>

'''XML
<block xmlns="https://developers.google.com/blockly/xml" type="helper_code_section">
  <statement name="statements">
    <block type="variable_create_set">
      <value name="variable_name">
        <block type="primitive_string">
          <field name="VALUE">request_data</field>
        </block>
      </value>
      <value name="variable_value">
        <block type="share_input">
          <value name="data">
            <block type="primitive_string">
              <field name="VALUE">fbfc447d312fa9f99f63b5bd94827d9a</field>
            </block>
          </value>
        </block>
      </value>
      <next>
        <block type="variable_create_set">
          <value name="variable_name">
            <block type="primitive_string">
              <field name="VALUE">url</field>
            </block>
          </value>
          <value name="variable_value">
            <block type="collection_hashmap-get">
              <mutation xmlns="http://www.w3.org/1999/xhtml" items="3"></mutation>
              <value name="array">
                <block type="primitive_string">
                  <field name="VALUE">request_data</field>
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
                  <field name="VALUE">url</field>
                </block>
              </value>
            </block>
          </value>
          <next>
            <block type="variable_create_set">
              <value name="variable_name">
                <block type="primitive_string">
                  <field name="VALUE">data</field>
                </block>
              </value>
              <value name="variable_value">
                <block type="collection_hashmap-get">
                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="3"></mutation>
                  <value name="array">
                    <block type="primitive_string">
                      <field name="VALUE">request_data</field>
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
                      <field name="VALUE">data</field>
                    </block>
                  </value>
                </block>
              </value>
              <next>
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
                            <block type="variable_get">
                              <value name="variable_name">
                                <block type="primitive_string">
                                  <field name="VALUE">url</field>
                                </block>
                              </value>
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
                          <mutation xmlns="http://www.w3.org/1999/xhtml" items="2"></mutation>
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
                                  <field name="VALUE">template</field>
                                </block>
                              </value>
                              <value name="value">
                                <block type="collection_hashmap">
                                  <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                  <value name="ADD0">
                                    <block type="collection_pair">
                                      <value name="key">
                                        <block type="primitive_string">
                                          <field name="VALUE">outputs</field>
                                        </block>
                                      </value>
                                      <value name="value">
                                        <block type="collection_arraylist">
                                          <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                          <value name="ADD0">
                                            <block type="collection_hashmap">
                                              <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                              <value name="ADD0">
                                                <block type="collection_pair">
                                                  <value name="key">
                                                    <block type="primitive_string">
                                                      <field name="VALUE">simpleText</field>
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
                                                            <block type="variable_get">
                                                              <value name="variable_name">
                                                                <block type="primitive_string">
                                                                  <field name="VALUE">data</field>
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
                </block>
              </next>
            </block>
          </next>
        </block>
      </next>
    </block>
  </statement>
</block>
'''

</details>

<details>
    <summary>response - body </summary>

'''XML
<block xmlns="https://developers.google.com/blockly/xml" type="response_context_create">
  <value name="status-code">
    <block type="primitive_integer">
      <field name="VALUE">200</field>
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
        <block type="parameter_create">
          <value name="key">
            <block type="primitive_string">
              <field name="VALUE">result</field>
            </block>
          </value>
          <value name="value">
            <block type="primitive_string">
              <field name="VALUE">ok</field>
            </block>
          </value>
          <value name="datatype">
            <block type="miscellaneous_parameter_type">
              <field name="parameter-type">string</field>
            </block>
          </value>
          <value name="description">
            <block type="primitive_string">
              <field name="VALUE">result</field>
            </block>
          </value>
          <value name="required">
            <block type="primitive_boolean">
              <field name="VALUE">false</field>
            </block>
          </value>
        </block>
      </value>
    </block>
  </value>
</block>
'''

</details>
