<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" simplifyDrawingHints="1" simplifyDrawingTol="1" minScale="100000000" styleCategories="AllStyleCategories" simplifyAlgorithm="0" simplifyMaxScale="1" version="3.16.5-Hannover" labelsEnabled="0" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal startField="" endExpression="" startExpression="" mode="0" endField="" durationField="" enabled="0" accumulate="0" durationUnit="min" fixedDuration="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 symbollevels="0" forceraster="0" type="singleSymbol" enableorderby="0">
    <symbols>
      <symbol name="0" type="line" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer class="SimpleLine" enabled="1" pass="0" locked="0">
          <prop k="align_dash_pattern" v="0"/>
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="dash_pattern_offset" v="0"/>
          <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="dash_pattern_offset_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="190,207,80,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.26"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="tweak_dash_pattern_on_corners" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>"TOK_ID"</value>
    </property>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks type="StringList">
      <Option value="" type="QString"/>
    </activeChecks>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field name="TOK_ID" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="MAX_UTOKJN" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="TOKREC_ID" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="IDVT" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="NAZ_TOK" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="SHAPE_LEN" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="TOK_ID" index="0"/>
    <alias name="" field="MAX_UTOKJN" index="1"/>
    <alias name="" field="TOKREC_ID" index="2"/>
    <alias name="" field="IDVT" index="3"/>
    <alias name="" field="NAZ_TOK" index="4"/>
    <alias name="" field="SHAPE_LEN" index="5"/>
  </aliases>
  <defaults>
    <default expression="" field="TOK_ID" applyOnUpdate="0"/>
    <default expression="" field="MAX_UTOKJN" applyOnUpdate="0"/>
    <default expression="" field="TOKREC_ID" applyOnUpdate="0"/>
    <default expression="" field="IDVT" applyOnUpdate="0"/>
    <default expression="" field="NAZ_TOK" applyOnUpdate="0"/>
    <default expression="" field="SHAPE_LEN" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" notnull_strength="0" field="TOK_ID" exp_strength="0" constraints="0"/>
    <constraint unique_strength="0" notnull_strength="0" field="MAX_UTOKJN" exp_strength="0" constraints="0"/>
    <constraint unique_strength="0" notnull_strength="0" field="TOKREC_ID" exp_strength="0" constraints="0"/>
    <constraint unique_strength="0" notnull_strength="0" field="IDVT" exp_strength="0" constraints="0"/>
    <constraint unique_strength="0" notnull_strength="0" field="NAZ_TOK" exp_strength="0" constraints="0"/>
    <constraint unique_strength="0" notnull_strength="0" field="SHAPE_LEN" exp_strength="0" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="TOK_ID"/>
    <constraint desc="" exp="" field="MAX_UTOKJN"/>
    <constraint desc="" exp="" field="TOKREC_ID"/>
    <constraint desc="" exp="" field="IDVT"/>
    <constraint desc="" exp="" field="NAZ_TOK"/>
    <constraint desc="" exp="" field="SHAPE_LEN"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column name="TOK_ID" type="field" hidden="0" width="-1"/>
      <column name="MAX_UTOKJN" type="field" hidden="0" width="-1"/>
      <column name="TOKREC_ID" type="field" hidden="0" width="-1"/>
      <column name="IDVT" type="field" hidden="0" width="-1"/>
      <column name="NAZ_TOK" type="field" hidden="0" width="-1"/>
      <column name="SHAPE_LEN" type="field" hidden="0" width="-1"/>
      <column type="actions" hidden="1" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable/>
  <labelOnTop/>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"TOK_ID"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
