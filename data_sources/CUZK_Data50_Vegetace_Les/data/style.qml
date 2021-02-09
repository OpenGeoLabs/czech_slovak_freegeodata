<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.12.2-București" simplifyDrawingTol="1" minScale="100000000" labelsEnabled="0" simplifyDrawingHints="1" simplifyMaxScale="1" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" readOnly="0" maxScale="0" simplifyAlgorithm="0" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" enableorderby="0" forceraster="0" type="singleSymbol">
    <symbols>
      <symbol clip_to_extent="1" name="0" type="fill" alpha="1" force_rhr="0">
        <layer pass="0" class="SimpleFill" enabled="1" locked="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="230,230,160,255" k="color"/>
          <prop v="miter" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="178,178,178,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
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
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory sizeScale="3x:0,0,0,0,0,0" barWidth="5" diagramOrientation="Up" minScaleDenominator="0" opacity="1" enabled="0" penWidth="0" spacingUnitScale="3x:0,0,0,0,0,0" spacing="5" backgroundAlpha="255" lineSizeType="MM" rotationOffset="270" width="15" penAlpha="255" scaleDependency="Area" direction="0" scaleBasedVisibility="0" lineSizeScale="3x:0,0,0,0,0,0" showAxis="1" labelPlacementMethod="XHeight" backgroundColor="#ffffff" maxScaleDenominator="1e+08" sizeType="MM" penColor="#000000" minimumSize="0" spacingUnit="MM" height="15">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
      <axisSymbol>
        <symbol clip_to_extent="1" name="" type="line" alpha="1" force_rhr="0">
          <layer pass="0" class="SimpleLine" enabled="1" locked="0">
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" placement="1" zIndex="0" obstacle="0" linePlacementFlags="18" showAll="1" priority="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option name="QgsGeometryGapCheck" type="Map">
        <Option value="0" name="allowedGapsBuffer" type="double"/>
        <Option value="false" name="allowedGapsEnabled" type="bool"/>
        <Option value="" name="allowedGapsLayer" type="QString"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <referencedLayers/>
  <referencingLayers/>
  <fieldConfiguration>
    <field name="SHAPE_Leng">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="SHAPE_Area">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DATA50_K">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DATA50_P">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="SHAPE_Leng" index="0" name=""/>
    <alias field="SHAPE_Area" index="1" name=""/>
    <alias field="DATA50_K" index="2" name=""/>
    <alias field="DATA50_P" index="3" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="SHAPE_Leng" expression="" applyOnUpdate="0"/>
    <default field="SHAPE_Area" expression="" applyOnUpdate="0"/>
    <default field="DATA50_K" expression="" applyOnUpdate="0"/>
    <default field="DATA50_P" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="SHAPE_Leng" unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="SHAPE_Area" unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="DATA50_K" unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="DATA50_P" unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="SHAPE_Leng" exp="" desc=""/>
    <constraint field="SHAPE_Area" exp="" desc=""/>
    <constraint field="DATA50_K" exp="" desc=""/>
    <constraint field="DATA50_P" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column hidden="0" width="-1" name="SHAPE_Leng" type="field"/>
      <column hidden="0" width="-1" name="SHAPE_Area" type="field"/>
      <column hidden="0" width="-1" name="DATA50_K" type="field"/>
      <column hidden="0" width="-1" name="DATA50_P" type="field"/>
      <column hidden="1" width="-1" type="actions"/>
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
    <field editable="1" name="DATA50_K"/>
    <field editable="1" name="DATA50_P"/>
    <field editable="1" name="SHAPE_Area"/>
    <field editable="1" name="SHAPE_Leng"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="DATA50_K"/>
    <field labelOnTop="0" name="DATA50_P"/>
    <field labelOnTop="0" name="SHAPE_Area"/>
    <field labelOnTop="0" name="SHAPE_Leng"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>SHAPE_Leng</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
