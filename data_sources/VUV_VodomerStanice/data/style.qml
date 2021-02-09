<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" labelsEnabled="0" readOnly="0" simplifyLocal="1" simplifyDrawingTol="1" maxScale="0" simplifyDrawingHints="0" hasScaleBasedVisibilityFlag="0" simplifyMaxScale="1" simplifyAlgorithm="0" version="3.8.3-Zanzibar" minScale="1e+08">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" symbollevels="0" forceraster="0" type="singleSymbol">
    <symbols>
      <symbol name="0" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="72,123,182,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="50,87,128,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions" value="&quot;OBJECTID&quot;"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory maxScaleDenominator="1e+08" lineSizeType="MM" scaleDependency="Area" backgroundColor="#ffffff" sizeType="MM" enabled="0" lineSizeScale="3x:0,0,0,0,0,0" backgroundAlpha="255" height="15" opacity="1" minimumSize="0" diagramOrientation="Up" barWidth="5" scaleBasedVisibility="0" labelPlacementMethod="XHeight" penColor="#000000" rotationOffset="270" sizeScale="3x:0,0,0,0,0,0" width="15" penAlpha="255" penWidth="0" minScaleDenominator="0">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" field="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="0" obstacle="0" linePlacementFlags="18" zIndex="0" priority="0" showAll="1" dist="0">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="OBJECTID">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DBC">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="HYDROID">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="JUNCTIONID">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DBCN">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="X_COORD">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Y_COORD">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="OBJECTID"/>
    <alias index="1" name="" field="DBC"/>
    <alias index="2" name="" field="HYDROID"/>
    <alias index="3" name="" field="JUNCTIONID"/>
    <alias index="4" name="" field="DBCN"/>
    <alias index="5" name="" field="X_COORD"/>
    <alias index="6" name="" field="Y_COORD"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="OBJECTID" applyOnUpdate="0"/>
    <default expression="" field="DBC" applyOnUpdate="0"/>
    <default expression="" field="HYDROID" applyOnUpdate="0"/>
    <default expression="" field="JUNCTIONID" applyOnUpdate="0"/>
    <default expression="" field="DBCN" applyOnUpdate="0"/>
    <default expression="" field="X_COORD" applyOnUpdate="0"/>
    <default expression="" field="Y_COORD" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0" field="OBJECTID"/>
    <constraint exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0" field="DBC"/>
    <constraint exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0" field="HYDROID"/>
    <constraint exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0" field="JUNCTIONID"/>
    <constraint exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0" field="DBCN"/>
    <constraint exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0" field="X_COORD"/>
    <constraint exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0" field="Y_COORD"/>
  </constraints>
  <constraintExpressions>
    <constraint field="OBJECTID" desc="" exp=""/>
    <constraint field="DBC" desc="" exp=""/>
    <constraint field="HYDROID" desc="" exp=""/>
    <constraint field="JUNCTIONID" desc="" exp=""/>
    <constraint field="DBCN" desc="" exp=""/>
    <constraint field="X_COORD" desc="" exp=""/>
    <constraint field="Y_COORD" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="&quot;DBC&quot;" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column name="OBJECTID" hidden="0" type="field" width="-1"/>
      <column name="DBC" hidden="0" type="field" width="-1"/>
      <column name="HYDROID" hidden="0" type="field" width="-1"/>
      <column name="JUNCTIONID" hidden="0" type="field" width="-1"/>
      <column name="DBCN" hidden="0" type="field" width="-1"/>
      <column name="X_COORD" hidden="0" type="field" width="-1"/>
      <column name="Y_COORD" hidden="0" type="field" width="-1"/>
      <column hidden="1" type="actions" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="DBC" editable="1"/>
    <field name="DBCN" editable="1"/>
    <field name="HYDROID" editable="1"/>
    <field name="JUNCTIONID" editable="1"/>
    <field name="OBJECTID" editable="1"/>
    <field name="X_COORD" editable="1"/>
    <field name="Y_COORD" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="DBC" labelOnTop="0"/>
    <field name="DBCN" labelOnTop="0"/>
    <field name="HYDROID" labelOnTop="0"/>
    <field name="JUNCTIONID" labelOnTop="0"/>
    <field name="OBJECTID" labelOnTop="0"/>
    <field name="X_COORD" labelOnTop="0"/>
    <field name="Y_COORD" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OBJECTID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
